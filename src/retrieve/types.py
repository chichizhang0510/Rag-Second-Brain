# 让类型注解延迟求值（以字符串形式处理），避免前向引用/导入顺序问题；在 3.10+ 常用，基本属于“类型系统友好设置”。
from __future__ import annotations

# 引入 dataclass 装饰器，用来自动生成 __init__、__repr__、__eq__ 等样板代码。
from dataclasses import dataclass

# Retrieval 对外承诺的结果形状
# 实例不可变。创建后不能改字段，防止下游误改检索结果（例如把 score 改掉）。这对调试和可复现很有帮助。
@dataclass(frozen=True)
class RetrievalHit:  # 定义“单条检索命中结果”对象。
    """A scored retrieval result mapped from a chunk."""

    chunk_id: str # 唯一标识符
    source: str # 源文件名
    heading: str # 当前节主标题
    heading_path: str # 可选，面包屑，供展示与日志。
    text: str # 参与检索的正文（可拼接 `heading_path` 进检索域以增强主题词命中，见 4.4）。  
    score: float # 得分

# 检索可调参数集合（top_k/min_score/...）
@dataclass(frozen=True)
class RetrievalConfig: # 定义“检索配置”对象。
    """Config knobs for retrieval behavior."""

    top_k: int = 5 # 返回条数上限
    min_score: float = 0.0 # 低于则丢弃（BM25 需按语料标定，可先 `0.0` 或分位数）
    max_chunk_chars: int | None = None # 单块进入索引前的截断（尾部截断并加省略标记或静默截断）
    include_heading_in_index_text: bool = True # 是否在参与 BM25 的字符串中重复标题路径
