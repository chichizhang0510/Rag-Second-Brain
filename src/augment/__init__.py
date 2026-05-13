"""Prompt augmentation layer for RAG."""

from src.augment.builder import build_messages
from src.augment.types import AugmentOptions

__all__ = ["build_messages", "AugmentOptions"]