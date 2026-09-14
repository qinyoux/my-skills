# board-cy 实例化指南 —— 为一块新板建立板级合同

> 本 Skill 是模板；本指南把模板实例化到一块具体开发板。产出 = 一份 `board-contract.json` + 一组 `references/*.md`，作为该板在后续开发/诊断/评审中的权威硬件上下文。

## 0 · 前置条件（缺一不可）

- 当前板的**原理图**与**引脚数据手册**（SoC 手册）。
- 能接触实物（用于确认 BOOT 行为、按键/丝印、电源开关等可观察事实）。
- 若已有已知缺口或历史批次问题，一并收集。
- 明确「硬件负责人」是谁——`board-contract.json` 的 `verified_at`/`authority` 字段需要真实来源。

## 1 · 建立实例目录

在目标工程（或独立资料库）内建立本 Skill 的实例目录。推荐把模板实例化到工程根：

```
<项目>/boards/<板型标识>/
├── board-contract.json          # 机器可读合同（本指南第 2 步产出）
├── identity-and-authority.md
├── pinout.md
├── boot-flash-recovery.md
├── power-and-peripherals.md
├── project-boundaries.md
└── known-gaps-and-errata.md
```

`<板型标识>` 用固件里使用的板型别名（如 `v2`）。目标工程引用本 Skill 时，通过 `--contract` 或约定路径指向这份 `board-contract.json`。

## 2 · 填合同（board-contract.json）

按 `references/board-contract.schema.json` 的字段语义填写。要点：

- **只填硬件事实**，不填项目策略（动作语义、协议、分区、休眠策略等一律归项目层）。
- **每个值都要有来源**：来自原理图、手册、实物确认或硬件负责人确认；来源不明的值留空或标 `UNKNOWN`，不得猜测。
- 必须包含 `scripts/check_board_baseline.py` 依赖的字段：`boot0`、`usb_dn/usb_dp`、`peripheral_power` 与各 `*_active_level`、`keys_active_low`、`board_aliases` 等；缺字段会让扫描器报 `board contract is missing required fields`。
- `verified_at` 填硬件负责人确认日期；`authority` 填确认主体与方式。

## 3 · 写 references（每份模板见本 Skill 的 references/ 目录）

- `identity-and-authority.md` — 身份、所有别名、证据优先级、被取代说法。
- `pinout.md` — 全部关键 GPIO 的映射、方向、有效电平、信号名、丝印。
- `boot-flash-recovery.md` — 进入/退出下载模式、恢复正常启动的唯一正确操作、板上按键清单。
- `power-and-peripherals.md` — 电源域、共享外设、唤醒/睡眠、USB/音频等。
- `project-boundaries.md` — 板级事实与项目策略的边界声明。
- `known-gaps-and-errata.md` — 已知缺口、历史冲突、批次风险。

## 4 · 只读核对与测试

```bash
# 扫描目标工程源码声明与合同的一致性（只读，不写设备）
python scripts/check_board_baseline.py <项目目录> --contract <board-contract.json>

# skill 合同测试（校验 SKILL.md/结构/合同字段）
python -m pytest tests/test_skill_contract.py
python -m pytest tests/test_check_board_baseline.py
```

- `FAIL` → 修正合同或拿到新硬件证据后再继续；`WARN` → 记录为待确认，不自动改写。
- 脚本退出 0 只表示无已建模 FAIL，不证明电气安全或真机行为。

## 5 · 接入项目与收尾

- 在项目 AGENTS/CLAUDE 入口或 flow 中登记「当前板 = <板型标识> → 合同路径」，让后续 Agent 知道用哪份合同。
- 把「未确认项」写进 `known-gaps-and-errata.md`，保持诚实标记 UNKNOWN。
- 新板实物行为与合同冲突时，按 SKILL.md「事实冲突处理」的优先级修订合同，并记录被取代关系。

## 质量门禁（每步自查）

- 合同里没有项目策略字段混入。
- 每个引脚/电源/BOOT 值都有来源且可追溯。
- BOOT/恢复操作只有一份真值，通用教程被明确标记为不适用。
- 完整测试运行过：`check_board_baseline.py` + 两个 pytest。
- 别名不指向多套电气设计；UNKNOWN 项仍为 UNKNOWN。
