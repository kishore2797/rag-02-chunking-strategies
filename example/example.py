#!/usr/bin/env python3
"""
RAG Tutorial 02 — Chunking Strategies
Minimal example: fixed-size and recursive (paragraph/sentence) chunking.
Run: python example.py (no extra deps)
"""
import re
from typing import List


def chunk_fixed_size(text: str, chunk_size: int = 200, overlap: int = 50) -> List[dict]:
    """Split text into fixed-size chunks with optional overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk_text = text[start:end]
        if chunk_text.strip():
            chunks.append({"text": chunk_text.strip(), "start": start, "end": end})
        start = end - overlap if overlap < chunk_size else end
    return chunks


def chunk_recursive(text: str, max_chunk_chars: int = 300) -> List[dict]:
    """Split by paragraph first, then by sentence, then by character."""
    if not text.strip():
        return []

    # Level 1: split by double newline (paragraphs)
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    current = []
    current_len = 0

    for para in paragraphs:
        if current_len + len(para) + 2 <= max_chunk_chars:
            current.append(para)
            current_len += len(para) + 2
        else:
            if current:
                chunks.append({"text": "\n\n".join(current), "strategy": "paragraph"})
            # If single para is too big, split by sentence
            if len(para) > max_chunk_chars:
                sentences = re.split(r'(?<=[.!?])\s+', para)
                for s in sentences:
                    if len(s) > max_chunk_chars:
                        for c in chunk_fixed_size(s, max_chunk_chars, 0):
                            c["strategy"] = "fixed"
                            chunks.append(c)
                    else:
                        chunks.append({"text": s, "strategy": "sentence"})
                current, current_len = [], 0
            else:
                current, current_len = [para], len(para) + 2
    if current:
        chunks.append({"text": "\n\n".join(current), "strategy": "paragraph"})
    return chunks


if __name__ == "__main__":
    sample = (
        "RAG Tutorial 02. Chunking matters. "
        "If chunks are too big, the LLM gets noise. If too small, context is lost.\n\n"
        "Fixed-size chunking is simple. Recursive chunking respects paragraphs and sentences."
    )
    print("Fixed-size (size=80, overlap=20):")
    for i, c in enumerate(chunk_fixed_size(sample, 80, 20)):
        print(f"  [{i}] {repr(c['text'][:60])}...")
    print("\nRecursive (max_chunk_chars=100):")
    for i, c in enumerate(chunk_recursive(sample, 100)):
        print(f"  [{i}] [{c.get('strategy','?')}] {repr(c['text'][:50])}...")
