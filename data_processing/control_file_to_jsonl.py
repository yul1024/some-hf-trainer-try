"""
Transform raw dataset to jsonl files.
"""

from __future__ import annotations
from loguru import logger

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def transform_raw_dataset_to_jsonl(
    raw_df: pd.DataFrame,
    result_path: str | Path,
) -> list[dict]:
    ...

