# This code is defining a data class called `DataIngestionConfig` using the `dataclass` decorator from
# the `dataclasses` module. The class has four attributes: `root_dir`, `source_URL`,
# `local_data_file`, and `unzip_dir`, all of which have specific types. `Path` is a class from the
# `pathlib` module that represents a file system path. The `frozen=True` argument to the `dataclass`
# decorator makes the class immutable, meaning that its attributes cannot be changed after it is
# created.
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path