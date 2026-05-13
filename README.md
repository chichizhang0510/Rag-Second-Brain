# rag-practice1

练习项目：**RAG M1** — Markdown 分块、**BM25** 检索、上下文拼 prompt（augment），以及通过 **OpenAI 兼容 API** 生成回答。

分发名与包配置见根目录 [`pyproject.toml`](pyproject.toml)；更细的打包与 `src` 布局说明见 [`docs/design/Pyproject_Toml_Design.md`](docs/design/Pyproject_Toml_Design.md)。

## 环境要求

- **Python** ≥ 3.10

## 快速开始

### 1. 创建虚拟环境并安装

```bash
cd /path/to/rag_practice1
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip
pip install -e ".[dev]"
```

也可仅用依赖文件（测试依赖已写在 `requirements.txt` 中）：

```bash
pip install -r requirements.txt
# 若要以包方式运行 CLI，仍建议：pip install -e .
```

### 2. 配置 API 与模型

在仓库根目录创建 `.env`（勿提交；已在 `.gitignore` 中忽略）。变量说明见 [`docs/Environment_Setup_Guide.md`](docs/Environment_Setup_Guide.md)。

**常用变量：**

| 变量 | 说明 |
| --- | --- |
| `OPENAI_API_KEY` | 必填（非 `--dry-run` 调用模型时）。 |
| `OPENAI_BASE_URL` | 可选；自定义 OpenAI 兼容端点。 |
| `OPENAI_MODEL` | 可选；未传 `--model` 时使用。 |
| `OPENAI_TEMPERATURE` | 可选；未传 `--temperature` 时使用。 |
| `OPENAI_MAX_TOKENS` | 可选；未传 `--max-tokens` 时使用。 |
| `OPENAI_TIMEOUT` | 可选；请求超时（秒）。 |

代码内默认值（环境未覆盖时）可参考 `src/llm_client/config.py`（如模型默认 `gpt-4o-mini`）。

### 3. 运行 CLI

安装可编辑包后，可使用控制台脚本 **`rag-ask`**（定义在 `[project.scripts]`）：

```bash
rag-ask --question "什么是拓扑排序？"
```

等价入口：

```bash
python -m src.cli --question "什么是拓扑排序？"
```

**知识库目录**：默认使用仓库下的 [`knowledge_base/`](knowledge_base/)（Markdown）。可用 `--kb-dir` 指向其他根目录。

**不调模型、只看检索与拼好的 prompt**：

```bash
rag-ask --question "什么是拓扑排序？" --dry-run
```

**检索调试**（分数、路径、chunk 等打到 stderr）：

```bash
rag-ask --question "..." --debug
```

### CLI 参数摘要

| 参数 | 说明 |
| --- | --- |
| `--question` | **必填**；用户问题，进入 augment / 最终 prompt。 |
| `--query` | 可选；BM25 检索用语；省略则与 `--question` 相同。 |
| `--kb-dir` | 可选；知识库根路径；默认 `<repo>/knowledge_base`。 |
| `--top-k` | 检索条数，默认 `5`。 |
| `--language` | `zh` 或 `en`，默认 `en`。 |
| `--model` / `--temperature` / `--max-tokens` | 传给生成逻辑；部分可与环境变量配合。 |
| `--debug` | 打印检索调试信息。 |
| `--dry-run` | 不调用 LLM，仅构建消息。 |

更完整的流水线与设计说明见 [`docs/design/CLI_System_Design.md`](docs/design/CLI_System_Design.md) 与 [`docs/instructions/CLI_E2E_Implementation_Manual.md`](docs/instructions/CLI_E2E_Implementation_Manual.md)。

## 开发与测试

**运行全部测试**（与当前解释器一致，建议使用 `python -m pytest`）：

```bash
python -m pytest
```

**仅测 CLI 并查看覆盖率**（示例）：

```bash
python -m pytest tests/cli --cov=src/cli --cov-report=term-missing
```

`pytest` 配置见 [`pytest.ini`](pytest.ini)（`pythonpath = .`，测试目录为 `tests/`）。

## 仓库结构（概要）

| 路径 | 作用 |
| --- | --- |
| `src/cli/` | 命令行入口、参数解析、流水线编排 |
| `src/chunking/` | Markdown 分块 |
| `src/retrieve/` | BM25 检索与流水线 |
| `src/augment/` | 上下文与 prompt 构建 |
| `src/llm_client/` | OpenAI 兼容客户端与配置 |
| `knowledge_base/` | 示例 Markdown 语料 |
| `tests/` | 各模块单元测试 |
| `docs/` | 设计说明、实施手册、复盘与环境文档 |
| `scripts/` | 辅助脚本 |

## 文档索引

- **环境与密钥**：[`docs/Environment_Setup_Guide.md`](docs/Environment_Setup_Guide.md)
- **打包与 `pyproject.toml`**：[docs/design/Pyproject_Toml_Design.md](docs/design/Pyproject_Toml_Design.md)
- **CLI 设计**：[docs/design/CLI_System_Design.md](docs/design/CLI_System_Design.md)
- **整体计划**：[docs/plan/Plan.md](docs/plan/Plan.md)
- **M1 复盘（架构与检索策略）**：[docs/problems/RAG_M1_Retrospective.md](docs/problems/RAG_M1_Retrospective.md)

各子模块（分块、检索、增强、生成）的实施手册在 `docs/instructions/` 下，可按文件名对应功能查阅。
