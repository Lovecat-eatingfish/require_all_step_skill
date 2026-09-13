# My Coding Skills

Claude Code 自定义 Skill 集合，用于提升 AI 辅助开发的流程规范性和输出质量。

## 目录结构

```
.
├── feature-delivery/           # 需求驱动开发全流程 Skill
│   ├── SKILL.md                # 主文件（流程定义 + 规则）
│   └── references/             # 按需加载的模板文件
│       ├── alignment-template.md      # 需求对齐确认单模板
│       ├── code-review-template.md    # 代码审查模板
│       ├── complexity-template.md     # 复杂度判断模板
│       ├── delivery-template.md       # 交付总结模板
│       └── requirement-card-template.md # 需求理解卡片模板
└── SKILL_DESIGN.md             # feature-delivery 的设计文档
```

## Skills 说明

### feature-delivery

需求驱动开发全流程 Skill。当用户提出功能需求、bug 修复、PRD 开发等需要写代码实现的请求时触发。

**流程**：判断复杂度（三档） → 读代码 → 读需求 → 对齐核心问题 → 开发 → 代码审查 → 测试交付。文书产出和提问轮次按 简单/普通/复杂 三档裁剪，验证质量不分档。

**核心约束（Iron Law）**：
1. 对齐前禁止写代码
2. 三要素不可省略（需求目标、验收标准、不做什么）
3. 范围变更需重新确认

**触发方式**：自动触发。用户提出任何开发类请求（实现需求、修 bug、加功能等）均适用；一句话能搞定的小改动走简单档快速通道，不强制全套文书。无法向用户提问时（后台任务、子代理），列出问题后按最优假设继续，假设在交付时逐条列出。

**测试策略**：接口/函数测试优先，静态验证补充，前端视觉交给人；测试前必须做副作用隔离，不污染真实用户数据。

## 安装使用

将 skill 目录复制到你的 skills 目录：

```bash
# Claude Code 全局安装（所有项目可用）
cp -r feature-delivery ~/.claude/skills/

# ZCode 用户级安装（所有项目可用）
cp -r feature-delivery ~/.agents/skills/

# 或项目级安装（仅当前项目可用）
cp -r feature-delivery .agents/skills/
```

使用时直接提出开发请求即可自动触发，也可手动指定：

```
/feature-delivery 帮我实现一个用户注册功能
```

## 设计原则

- **流程规范**：不跳过对齐直接写代码
- **档位缩放**：文书随复杂度缩放（简单/普通/复杂三档），验证质量不分档
- **务实测试**：能跑测试就跑，不能跑就静态验证，不假装能做所有事；测试不污染真实数据
- **遵循惯例**：代码风格向项目既有实现看齐
- **清晰交付**：按模板输出交付总结，无关章节标"不适用"，不硬凑内容

## 评估框架

基于四维度评估：

| 维度 | 说明 | 权重 |
|------|------|------|
| Outcome | 任务完成了没有 | 30% |
| Process | 路径走对了没有 | 30% |
| Style | 输出能不能接手 | 20% |
| Efficiency | 成本会不会失控 | 20% |

详见各 skill 的 SKILL.md 和 references/ 目录下的模板文件。
