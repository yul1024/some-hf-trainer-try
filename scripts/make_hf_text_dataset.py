"""
Transform raw dataset to jsonl files.

One time script.
"""

from __future__ import annotations
from loguru import logger

from data_processing.control_file_to_jsonl import transform_raw_dataset_to_jsonl

import polars as pl
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def main(
    control_file_path: str,
    txt_file_dir: str,
    result_path: str,
) -> None:
    control_df = pl.read_excel(
        source=control_file_path,
        schema_overrides={
            'Stkcd': pl.String,
            'Nnindnme': pl.Categorical,
            'Markettype': pl.Categorical,
            'OWNERSHIPTYPE': pl.Categorical,
        },
    )
    logger.trace(control_df)
    # print(control_df)
    # print(control_df.describe())
    df = transform_raw_dataset_to_jsonl(
        raw_df=control_df,
        txt_file_dir=txt_file_dir,
        file_type='txt',
    )
    logger.trace(df)
    df = df.select(
        pl.col('is_risk').alias('label'),
        pl.col('text'),
    )
    logger.trace(df)
    df.write_ndjson(result_path)


if __name__ == '__main__':
    main(
        control_file_path=r"D:\dataset\smart\original_data\all_in_one.xlsx",
        txt_file_dir=r"D:\dataset\smart\data_pipeline_cache\surveyor_cache",
        result_path=r"./all_data.jsonl",
    )

