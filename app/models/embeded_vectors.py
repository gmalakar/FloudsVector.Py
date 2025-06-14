# =============================================================================
# File: embeded_vectors.py
# Date: 2025-06-14
# Copyright (c) 2024 Goutam Malakar. All rights reserved.
# =============================================================================

from typing import List

from pydantic import BaseModel, Field


class EmbeddedVectors(BaseModel):
    chunk: str = Field(..., description="The text chunk.")
    model: str = Field(..., description="The model used for embedding.")
    vector: List[float] = Field(..., description="The embedding vector values.")
