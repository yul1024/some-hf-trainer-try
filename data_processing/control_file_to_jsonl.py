"""
Transform raw dataset to jsonl files.
"""

from __future__ import annotations
from loguru import logger

import polars as pl
import json
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def transform_raw_dataset_to_jsonl(
    raw_df: pl.DataFrame,
    txt_file_dir: str | Path,
    # result_path: str | Path,
    file_type: str,
) -> pl.DataFrame:
    # path processing
    txt_file_dir = Path(txt_file_dir)
    # result_path = Path(result_path)
    # result_path.parent.mkdir(parents=True, exist_ok=True)
    # file loading method
    def load_markdown(
        stock_code: str,
    ) -> str:
        markdown_file_path = Path(txt_file_dir) / f"{stock_code}.{file_type}"
        return Path(markdown_file_path).read_text(encoding='utf-8')
    # transform data
    result = raw_df.select(
        pl.col('Stkcd'),
        pl.col('is_risk'),
    ).with_columns(
        text=pl.col('Stkcd').map_elements(load_markdown, return_dtype=pl.String),
    )
    return result

