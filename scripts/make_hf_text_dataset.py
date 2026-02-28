"""
Transform raw dataset to jsonl files.

One time script.
"""

from __future__ import annotations
from loguru import logger

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def main(
    control_file_path: str,
    txt_file_dir: str,
    result_dir: str,
) -> None:
    ...


if __name__ == '__main__':
    main(
        control_file_path=r"D:\dataset\smart\original_data\all_in_one.xlsx",
        txt_file_dir=r"D:\dataset\smart\data_pipeline_cache\surveyor_cache",
        result_dir=r"D:\dataset\smart\t",
    )

