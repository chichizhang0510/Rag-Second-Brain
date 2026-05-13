"""
Tokenize text for retrieval.

tokenize 就是把文本转成 token 列表。
BM25 要求 query/corpus 采用一致 token 化。
中文单字切分虽然粗糙，但 M1 足够；M2 可以升级到 jieba 或 embedding。

实现原则：先“可用”，再“精细”。M1 推荐简单稳妥规则：
- 英文：按单词切分
- 中文：按单字切分（不引入额外依赖）
- 统一小写

以后要改 jieba、2-gram、甚至子词分词，只改 tokenize.py。
"""

from __future__ import annotations

# 导入正则库，后面要用 re.compile 和 findall 做分词。
import re

# 英文：按单词切分
# 连续的 a-z 或 0-9 组成一个 token。
# + 表示前面一个或多个。
EN_RE = re.compile(r"[a-z0-9]+")
# 中文：按单字切分（不引入额外依赖）
# 中日韩越统一汉字 Unicode 范围：[\u4e00-\u9fff]
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
# 用 compile 而不是每次现写正则，性能和可读性都更好。

def tokenize(text: str) -> list[str]:  # 定义统一分词函数。
    """
    Minimal bilingual tokenizer for BM25:
    - English/alnum words
    - CJK single characters
    """
    lower = text.lower()  # 统一小写，减少大小写差异造成的“假不匹配”。
    en_tokens = EN_RE.findall(lower)  # 在文本里提取所有英文/数字 token。findall 会返回所有匹配到的片段列表。
    cjk_tokens = CJK_RE.findall(lower)  # 在文本里提取所有汉字 token。
    return en_tokens + cjk_tokens  # 把两类 token 合并返回给 BM25。返回顺序本身不太关键（BM25主要看词频/文档频率），关键是“同规则”。