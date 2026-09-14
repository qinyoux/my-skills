---
name: submit-skill-to-git
description: 当需要向 my-skills GitHub 仓库提交新 Skill、更新现有 Skill 或同步 Skill 仓库时使用此 skill。它提供完整的标准操作流程（SOP），包括 clone、创建分支、提交、推送、创建 PR 的命令模板和规范要求。
---

# submit-skill-to-git

向 `qinyoux/my-skills` 仓库提交/更新 Skill 的标准操作手册。

## 触发条件

当需要执行以下操作时使用此 skill：

- 向 my-skills 仓库**提交新 Skill**
- **更新**仓库中已有的 Skill
- **同步**本地仓库到最新版本
- 查询仓库中的 Skill 列表

## 前置准备

### 1. 确认 gh CLI 已认证

```bash
gh auth status
```

输出应显示 `✓ Logged in to github.com`。未登录则先执行 `gh auth login`。

### 2. 确认有仓库访问权限

```bash
gh repo view qinyoux/my-skills
```

---

## 操作流程

### 场景一：提交新 Skill

#### 1. Clone 仓库（如尚未 clone）

```bash
gh repo clone qinyoux/my-skills
cd my-skills
```

#### 2. 同步到最新

```bash
git checkout main
git pull origin main
```

#### 3. 创建 feature 分支

```bash
git checkout -b feat/add-<skill名>
```

#### 4. 创建 Skill 目录结构

在 `skills/` 下创建目录，放入 `SKILL.md`（必需）及其他可选文件：

```
skills/<skill名>/
├── SKILL.md          （必需）
├── references/       （可选）
├── scripts/          （可选）
├── tests/            （可选）
└── assets/           （可选）
```

#### 5. 提交

```bash
git add skills/<skill名>/
git commit -m "feat: add <skill名>"
```

#### 6. 推送

```bash
git push -u origin feat/add-<skill名>
```

#### 7. 创建 PR

```bash
gh pr create --title "feat: add <skill名>" --body "新增 skill: <简介>"
```

#### 8. 等待 Review 和合并

---

### 场景二：更新现有 Skill

#### 1. 同步到最新

```bash
git checkout main
git pull origin main
```

#### 2. 创建更新分支

```bash
git checkout -b update/<skill名>-<修改说明>
```

#### 3. 修改文件

编辑 `skills/<skill名>/` 下的相关文件。

#### 4. 提交

```bash
git add skills/<skill名>/
git commit -m "update: <skill名> - <修改说明>"
```

#### 5. 推送 + 创建 PR

```bash
git push -u origin update/<skill名>-<修改说明>
gh pr create --title "update: <skill名> - <修改说明>" --body "<改动详情>"
```

#### 6. 等待合并

---

### 场景三：修复 Skill 中的问题

```bash
git checkout main
git pull origin main
git checkout -b fix/<skill名>-<问题描述>
# 修改文件
git add skills/<skill名>/
git commit -m "fix: <skill名> - <问题描述>"
git push -u origin fix/<skill名>-<问题描述>
gh pr create --title "fix: <skill名> - <问题描述>" --body "<修复说明>"
```

---

### 场景四：同步本地仓库

```bash
git checkout main
git pull origin main
```

---

## 规范要求

### 分支命名

| 操作类型 | 格式 | 示例 |
|---|---|---|
| 新增 Skill | `feat/add-<名>` | `feat/add-mqtt-skill` |
| 更新 Skill | `update/<名>-<说明>` | `update/board-cy-add-board` |
| 修复问题 | `fix/<名>-<问题>` | `fix/esp-idf-cy-port-detection` |
| 文档 | `docs/<说明>` | `docs/update-readme` |

### Commit Message（Conventional Commits）

- `feat:` 新增功能/Skill
- `update:` 更新现有内容
- `fix:` 修复问题
- `docs:` 文档更新

### PR 要求

- main 分支已保护，**禁止直接 push**
- 必须通过 PR，至少 1 人 approve
- PR title 简明，body 说明改动内容和原因

### SKILL.md 必须包含

```markdown
---
name: <skill名>
description: <一句话描述用途和触发条件>
---

# <Skill 名称>

## 触发条件
<什么场景下使用>

## 使用说明
<操作步骤和命令模板>
```

### 文件清理

- 不要提交 `__pycache__/`、`.pyc` 文件
- 不要提交临时输出文件
- 确保 `.gitignore` 已配置

---

## 不负责

- 本 skill 不负责编写 Skill 的具体业务内容（那是各 skill 自身的职责）
- 本 skill 不负责 GitHub 账户注册或权限申请
- 本 skill 不负责 CI/CD 配置
