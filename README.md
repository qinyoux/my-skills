# my-skills

TRAE 自定义 Skills 共享仓库 —— 用于多 Agent 协作场景下的 Skill 统一管理与分发。

## 仓库用途

本仓库集中管理 TRAE 平台上的自定义 Skills，便于：

- **多 Agent 协作**：不同 AI Agent 可以 clone 本仓库，加载所需 Skill
- **版本管理**：通过 Git 实现 Skill 的版本追踪与回滚
- **标准化贡献**：任何 Agent 遵循 [CONTRIBUTING.md](CONTRIBUTING.md) 即可提交新 Skill 或更新现有 Skill

## 仓库结构

```
my-skills/
├── README.md                          仓库总说明（本文件）
├── CONTRIBUTING.md                    贡献指南（标准操作手册 SOP）
├── skills/
│   ├── submit-skill-to-git/           SOP Skill —— 提交 Skill 到 Git 的标准流程
│   │   └── SKILL.md
│   ├── board-cy/                      嵌入式开发板板级合同 Skill
│   ├── esp-idf-cy/                    ESP-IDF 一站式开发 Skill
│   ├── project-flow-cy/               多 Agent 协作流程 Skill
│   └── wechat-typesetting-trae-main/  微信公众号排版 Skill
```

## 包含的 Skills

| Skill 名称 | 说明 |
|---|---|
| `submit-skill-to-git` | SOP Skill —— 指导 Agent 如何向本仓库提交/更新 Skill |
| `board-cy` | 嵌入式开发板板级合同，固化板子身份、引脚、BOOT 规则、安全边界 |
| `esp-idf-cy` | ESP-IDF 一站式开发，自动检测/安装环境、编译、烧录、串口验证 |
| `project-flow-cy` | 基于 flow/ + docs/ 的多 Agent 协作流程管理 |
| `wechat-typesetting-trae-main` | 微信公众号文章多模板排版 |

## 快速使用

其他 Agent 克隆并使用本仓库中的 Skill：

```bash
# Clone 仓库
gh repo clone qinyoux/my-skills
cd my-skills

# 将所需 skill 复制到 TRAE skills 目录
# Windows 示例：
Copy-Item -Recurse skills/board-cy "$env:USERPROFILE\.trae-cn\skills\"
```

加载 Skill 后，在 TRAE 对话中直接触发即可。

## 贡献流程

要提交新 Skill 或更新现有 Skill，请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 获取完整的标准操作手册。

简要流程：创建分支 → 修改文件 → 提交 → 推送 → 创建 PR → 等待 Review。

## 许可

本仓库中的 Skills 由各自作者贡献，供 TRAE 社区使用。
