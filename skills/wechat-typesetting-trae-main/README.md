# ✍️ wechat-typesetting-cy — Trae 可用的微信公众号多模板排版技能

将纯文本或 Markdown 自动转换为精美排版的 HTML，直接复制粘贴到公众号编辑器即可发布。

本仓库已调整为可直接作为 Trae 的自定义 Skill 使用，核心入口文件仍为 `SKILL.md`。

## 功能特性

- **多模板支持** — 内置两套视觉风格，覆盖不同类型文章
- **自动选模板** — 根据文章内容智能匹配最合适的模板
- **全内联样式** — 生成的 HTML 完全兼容微信公众号编辑器
- **浏览器预览** — 在当前环境允许时自动打开浏览器预览排版效果
- **排版检查** — 对已有 HTML 进行规范性检查并给出改进建议

## 可用模板

| 模板 | 视觉风格 | 适合内容 |
|------|----------|----------|
| `blue-minimal` | 白底蓝色，衬线字体，杂志感 | 深度分析、思考、随笔、观点文 |
| `dark-tech` | 黑底橙红，无衬线，卡片化 | 产品介绍、科技报道、数据驱动 |

## 安装使用

### 添加为 Trae Skill

```bash
# 方式一：将本文件夹或 ZIP 包导入 Trae 的 Skills
# 保留 SKILL.md、assets/、references/ 目录结构即可

# 方式二：手动放入 Trae 的本地 skills 目录
# 例如：<你的项目>/.trae/skills/wechat-typesetting-cy/
# 然后重启或重新加载 Trae
```

> 说明：Trae 已支持基于 `SKILL.md` 的开放 Skill 结构，因此不需要 `claude skill add` 之类的 Claude 专属命令。

### 触发方式

在 Trae 对话中使用以下关键词即可触发：

- "帮我排版"、"公众号排版"、"排版成微信格式"
- "蓝色模板"、"暗黑模板"、"科技风排版"
- "微信文章"、"公众号文章"、"发公众号"

### 使用流程

1. 给 Trae 你的文章内容（纯文本或 Markdown）
2. 技能自动选择合适模板（也可手动指定）
3. 生成排版后的 HTML 文件，保存到 `output/` 目录
4. 在当前系统默认浏览器中打开预览（如果环境允许）
5. 选中内容 → 复制 → 粘贴到公众号编辑器

## 目录结构

```
wechat-typesetting-cy/
├── SKILL.md                        # Trae Skill 定义
├── README.md
├── .gitignore
├── assets/
│   ├── wechat-qr.jpg              # 联系二维码
│   └── templates/                  # HTML 模板文件
│       ├── blue-minimal.html      # 蓝色极简模板
│       └── dark-tech.html         # 暗黑科技模板
├── references/                     # 样式规范文档
│   ├── guidelines.md              # 通用排版规范
│   ├── blue-minimal.md            # 蓝色极简样式规范
│   └── dark-tech.md               # 暗黑科技样式规范
└── output/                         # 排版输出目录（运行时生成，不纳入版本控制）
```

## 扩展新模板

添加新模板只需 3 步：

1. 添加 `assets/templates/{模板名}.html` — HTML 模板文件
2. 添加 `references/{模板名}.md` — 样式规范文档
3. 在 `SKILL.md` 的"可用模板"表格和"组件映射"部分添加对应内容

## 许可证

MIT License

---

<div align="center">
  <h3>联系作者</h3>
  <p>扫码加微信，交流反馈</p>
  <img src="assets/wechat-qr.jpg" alt="WeChat QR Code" width="200">
</div>
