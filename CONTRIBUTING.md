# 贡献指南 —— 向 my-skills 仓库提交 Skill 的标准操作手册（SOP）

本文件是任何 AI Agent 或人类贡献者向 `qinyoux/my-skills` 仓库提交、更新 Skill 的**标准操作手册**。阅读本文件后，你应能独立完成全部操作。

---

## A. 前置准备

### 1. 确认 gh CLI 已认证

```bash
gh auth status
```

输出应显示 `✓ Logged in to github.com`。如果未登录，先执行：

```bash
gh auth login
```

按提示选择 GitHub.com → HTTPS → 浏览器授权。

### 2. 确认仓库访问权限

```bash
gh repo view qinyoux/my-skills
```

能正常显示仓库信息即有访问权限。本仓库为 public，任何人可 clone；提交 PR 需要有 write 权限或先 fork。

### 3. 确认本地工具

- `git`（已随 gh CLI 安装时一并配置）
- `gh` CLI（用于创建 PR、查看仓库）
- 文本编辑能力（用于编写 SKILL.md）

---

## B. Clone 仓库

```bash
gh repo clone qinyoux/my-skills
cd my-skills
```

如果是外部贡献者（无 write 权限），先 fork 再 clone：

```bash
gh repo fork qinyoux/my-skills --clone
cd my-skills
```

---

## C. 添加新 Skill 的流程

### 1. 创建 feature 分支

```bash
git checkout -b feat/add-<skill名>
```

示例：`git checkout -b feat/add-mqtt-skill`

### 2. 创建 Skill 目录并放入文件

在 `skills/` 下创建新目录：

```
skills/
└── <skill名>/
    ├── SKILL.md          （必需 —— 核心文件）
    ├── references/       （可选 —— 参考文档）
    ├── examples/         （可选 —— 示例）
    └── scripts/          （可选 —— 脚本）
```

**SKILL.md 必须包含的字段：**

```markdown
---
name: <skill名>
description: <一句话描述 skill 用途和触发条件>
---

# <Skill 名称>

## 触发条件
<什么场景下应使用此 skill>

## 使用说明
<操作步骤、命令模板、注意事项>
```

### 3. 提交

```bash
git add skills/<skill名>/
git commit -m "feat: add <skill名>"
```

### 4. 推送

```bash
git push -u origin feat/add-<skill名>
```

### 5. 创建 PR

```bash
gh pr create --title "feat: add <skill名>" --body "新增 skill: <简介>"
```

### 6. 等待 Review 和合并

PR 创建后，仓库所有者会 review。合并后 Skill 即进入 main 分支。

---

## D. 更新现有 Skill 的流程

### 1. 确保本地是最新的

```bash
git checkout main
git pull origin main
```

### 2. 创建更新分支

```bash
git checkout -b update/<skill名>-<修改说明>
```

示例：`git checkout -b update/board-cy-add-new-board`

### 3. 修改文件

编辑 `skills/<skill名>/` 下的相关文件。

### 4. 提交

```bash
git add skills/<skill名>/
git commit -m "update: <skill名> - <修改说明>"
```

### 5. 推送 + 创建 PR

```bash
git push -u origin update/<skill名>-<修改说明>
gh pr create --title "update: <skill名> - <修改说明>" --body "<改动详情>"
```

### 6. 等待合并

---

## E. 同步更新

当远程 main 有新提交时，同步本地：

```bash
git checkout main
git pull origin main
```

如果当前在 feature 分支上工作，想合并 main 的最新更改：

```bash
git checkout <你的分支>
git merge main
```

---

## F. PR 规范

### 分支命名

| 操作类型 | 命名格式 | 示例 |
|---|---|---|
| 新增 Skill | `feat/add-<名>` | `feat/add-mqtt-skill` |
| 更新 Skill | `update/<名>-<说明>` | `update/board-cy-add-new-board` |
| 修复问题 | `fix/<名>-<问题>` | `fix/esp-idf-cy-port-detection` |
| 文档更新 | `docs/<说明>` | `docs/update-readme` |

### Commit Message 规范

使用 Conventional Commits：

| 前缀 | 用途 | 示例 |
|---|---|---|
| `feat:` | 新增功能/Skill | `feat: add mqtt-skill` |
| `update:` | 更新现有内容 | `update: board-cy - add new board profile` |
| `fix:` | 修复问题 | `fix: esp-idf-cy port detection on Windows` |
| `docs:` | 文档更新 | `docs: update README with new skill` |

### PR 要求

- **PR title** 简明扼要，概括改动内容
- **PR body** 说明改动内容、原因、测试方式
- **不要直接 push 到 main 分支**（main 已设分支保护，必须通过 PR）
- PR 需至少 1 人 approve 后才能合并

---

## G. Skill 目录结构规范

每个 Skill 目录**必须**包含 `SKILL.md`，这是 Skill 的核心入口文件。

### 标准目录结构

```
skills/<skill名>/
├── SKILL.md              必需 —— Skill 描述、触发条件、使用说明
├── references/           可选 —— 详细参考文档（多文件可放此目录）
├── examples/             可选 —— 使用示例
├── scripts/              可选 —— 脚本文件（.sh / .py / .ps1 等）
├── tests/                可选 —— 测试文件
├── assets/               可选 —— 模板、图片等资源
└── evals/                可选 —— 评估配置
```

### SKILL.md 编写要求

1. **Frontmatter**：包含 `name` 和 `description`
2. **触发条件**：明确说明什么场景下应触发此 skill
3. **使用说明**：操作步骤清晰，包含可直接执行的命令模板
4. **边界说明**：说明此 skill 不负责什么，避免误用

### 注意事项

- 不要提交 `__pycache__/`、`.pyc` 文件，确保 `.gitignore` 已配置
- 不要提交临时输出文件
- 脚本文件需有可执行权限（`chmod +x`）
- 中文文件名允许，但建议用英文命名提高兼容性

---

## 常见问题

### Q: gh auth login 失败怎么办？

检查网络代理设置，或尝试使用 token 登录：

```bash
gh auth login --with-token < token.txt
```

### Q: git push 被拒绝（main 分支保护）？

这是预期行为。main 分支禁止直接 push，请创建 feature 分支走 PR 流程。

### Q: 如何查看自己已提交的 PR？

```bash
gh pr list --author @me
```
