# Project Story Doc

[![仓库校验](https://github.com/layinginbed/project-story-doc/actions/workflows/validate.yml/badge.svg)](https://github.com/layinginbed/project-story-doc/actions/workflows/validate.yml)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)](https://learn.chatgpt.com/docs/build-skills)
[![状态](https://img.shields.io/badge/status-usable-16a34a)](#项目状态)

**一个面向 Codex 的证据化项目认知 Skill。它用于创建和维护可信的项目、仓库、论文及论文加代码讲解文档。**

[English](README.md) · [安装](#安装) · [工作方式](#工作方式) · [参与贡献](CONTRIBUTING.md)

Project Story Doc 解决一个具体问题：怎样让读者的认知持续跟上项目或研究制品的真实现状。

它不会只总结目录和文件。它会冻结来源快照，区分当前实现、未来计划、证据推断和未知内容，追踪一条代表性执行链，检查系统结构与状态覆盖，并维护精简的当前文档集。

## 为什么需要这个 Skill

技术文档常见以下问题：

- 把设计意图写成已经运行的行为；
- 按目录讲源码，但不解释真正的执行过程；
- 混淆论文主张、发布代码和复现实验；
- 不断新建文档，却不确定哪一份是当前主入口；
- 在 dirty worktree 中写文档，却没有隔离本次修改；
- 把合理推断写成已经验证的事实。

Project Story Doc 把这些问题作为工作流约束处理，而不是只调整写作风格。

## 主要能力

| 能力 | Skill 的控制要求 |
|---|---|
| Create | 从一手来源建立一份可信的当前主入口。 |
| Refresh | 对照冻结的来源快照，原位刷新当前文档。 |
| Deep dive | 深入解释一个子系统、机制、实验或研究问题，并避免复制主文档。 |
| Organize history | 只把已确认过时的文档移动到可恢复的历史区域。 |
| 证据控制 | 区分制品明确事实、外部证据、推断和未知内容。 |
| 系统覆盖 | 覆盖关键元素、关系、状态字段、迁移和提交边界。 |
| 读者设计 | 围绕读者问题组织讲解，不套用固定目录模板。 |
| 安全 Apply | 保留原有 dirty worktree，限定写入路径，并核对本次实际变化。 |

## 工作方式

```mermaid
flowchart LR
    A["项目、仓库、论文或论文加代码"] --> B["冻结读者契约和来源快照"]
    B --> C["选择模式、路线、深度和执行姿态"]
    C --> D["建立证据和覆盖清单"]
    D --> E["解释结构、状态和一条代表性链路"]
    E --> F["把关键主张映射到验证与不确定性"]
    F --> G["创建或刷新最小当前文档集"]
    G --> H["回读并验证链接、视觉、范围和修改差异"]
```

每次运行先确定四项选择：

| 决策 | 可选值 |
|---|---|
| 运行模式 | `Create`、`Refresh`、`Deep dive`、`Organize history` |
| 执行姿态 | `Plan-only` 只检查和规划；`Apply` 执行已授权写入 |
| 制品路线 | `Project`、`Repository`、`Paper`、`Paper plus code` |
| 深度 | `Brief`、`Standard`、`Deep` |

运行模式和执行姿态彼此独立。可以只规划一次 Refresh，也可以在用户明确要求时 Apply 一次 Deep dive。

## 安装

Codex 当前从 `$HOME/.agents/skills` 加载个人 Skill，并支持符号链接。以下命令把 Git 仓库与 Skill 发现目录分开：

```bash
git clone https://github.com/layinginbed/project-story-doc.git \
  "$HOME/.local/share/project-story-doc"
mkdir -p "$HOME/.agents/skills"
ln -s "$HOME/.local/share/project-story-doc/project-story-doc" \
  "$HOME/.agents/skills/project-story-doc"
```

Codex 会自动检测 Skill 变化。如果 Skill 没有出现，请重启 Codex。当前规则见 OpenAI 官方文档：[构建和加载 Skills](https://learn.chatgpt.com/docs/build-skills)。

### 更新

```bash
git -C "$HOME/.local/share/project-story-doc" pull --ff-only
```

### 调用

可以显式写出 `$project-story-doc`。如果请求符合 Skill 的 `description`，Codex 也可以自动调用。

```text
$project-story-doc 为当前 checkout 创建一份 Standard 深度的项目和仓库讲解。先使用 Plan-only。
```

```text
$project-story-doc 根据当前 working tree 刷新已有文档。Apply 已批准的编辑范围，并保留无关修改。
```

```text
$project-story-doc 深入解释这个子系统的状态迁移和失败边界。分别标注实现、测试和推断。
```

## 制品路线

Skill 不会把所有对象强制写成同一种目录：

- **Project** 关注目标、用户、交付物、当前状态、决策和未完成工作。
- **Repository** 关注入口、运行行为、所有权、状态、接口、测试和失败路径。
- **Paper** 关注研究问题、相关工作、方法、证据、批判和后续研究。
- **Paper plus code** 分开论文主张、代码实现和实际复现状态。

持续迭代的软件项目通常以 Project 作为状态层，以 Repository 作为机制层。

## 证据模型

每个关键主张必须属于以下一类：

1. **制品明确**：目标制品直接说明、实现或展示。
2. **外部证据**：一手外部来源或官方文档支持。
3. **证据推断**：由已引用前提推导，但目标制品没有直接说明。
4. **尚不确定**：证据缺失、冲突、陈旧或仍未解决。

这套模型可以避免把“存在”“已启用”“正在使用”“可以工作”和“产生了声称的结果”混成一句没有证据边界的话。

## 文档数量控制

默认新增文档预算保持精简：

| 模式 | 默认最多新增当前叙事文档数 |
|---|---:|
| Create | 2 |
| Refresh | 0 |
| Deep dive | 1 |
| Organize history | 0 |

该预算不是正确性的硬上限。它要求每一份额外文档都说明独立读者问题、证据边界、长期维护价值和入口链接。

## 仓库结构

```text
.
├── README.md
├── README.zh-CN.md
├── CONTRIBUTING.md
├── SECURITY.md
├── scripts/
│   └── validate_repository.py
└── project-story-doc/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        ├── operating-modes-and-lifecycle.md
        ├── document-archetypes.md
        ├── evidence-model.md
        ├── system-coverage.md
        ├── reasoning-reconstruction.md
        ├── visual-explanation.md
        ├── attack-and-follow-up.md
        └── writing-and-review.md
```

仓库根目录保存面向人的展示和协作材料。`project-story-doc/` 子目录保持为 Codex 实际加载的完整 Skill。

## 本地校验

仓库包含一个无第三方依赖的校验脚本。该脚本检查 Skill 元数据、必需文件、本地 Markdown 链接、目录边界和常见凭据格式。

```bash
python3 scripts/validate_repository.py
```

GitHub Actions 会对每次 push 和 pull request 执行相同校验。

## 项目状态

当前 Skill 包已通过格式和仓库校验，可以使用。项目、仓库、论文和论文加代码路线的场景级验证仍在持续进行。提交 issue 时，请区分已验证行为和未经测试的路线或深度，并提供运行模式、制品路线、来源边界，以及期望输出与实际输出之间的差异。

## 参与贡献

欢迎修正可泛化的行为类型，不接受只针对某一个私有案例的过拟合修改。提交 pull request 前，请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

不要在公开 issue 或测试材料中提交私有仓库内容、专有文档、凭据、原始用户数据或敏感 trace。安全说明见 [SECURITY.md](SECURITY.md)。

## 许可证

本仓库尚未选择开源许可证。仓库公开不等于自动授予复制、修改或再分发权。维护者明确选择授权条款后，再添加许可证文件。
