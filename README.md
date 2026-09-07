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

**流程**：读代码 → 读需求 → 对齐核心问题 → 开发 → 代码审查 → 测试交付

**核心约束（Iron Law）**：
1. 对齐前禁止写代码
2. 三要素不可省略（需求目标、验收标准、不做什么）
3. 范围变更需重新确认

**触发方式**：用户手动 `/feature-delivery` 触发

**测试策略**：接口/函数测试优先，静态验证补充，前端视觉交给人

## 安装使用

将 skill 目录复制到你的 Claude Code skills 目录：

```bash
# 全局安装（所有项目可用）
cp -r feature-delivery ~/.claude/skills/

# 或项目级安装（仅当前项目可用）
cp -r feature-delivery .claude/skills/
```

在 Claude Code 中使用：

```
/feature-delivery 帮我实现一个用户注册功能
```

## 设计原则

- **流程规范**：不跳过对齐直接写代码
- **务实测试**：能跑测试就跑，不能跑就静态验证，不假装能做所有事
- **遵循惯例**：代码风格向项目既有实现看齐
- **清晰交付**：按模板输出完整交付总结，不遗漏任何章节

## 评估框架

基于四维度评估：

| 维度 | 说明 | 权重 |
|------|------|------|
| Outcome | 任务完成了没有 | 30% |
| Process | 路径走对了没有 | 30% |
| Style | 输出能不能接手 | 20% |
| Efficiency | 成本会不会失控 | 20% |

详见各 skill 的 SKILL.md 和 references/ 目录下的模板文件。
