from dataclasses import dataclass


@dataclass
class Config:
    # CSV file delimiter
    delimiter: str
    # CSV quote character
    quote_character: str
    # Skip N lines at the beginning of the file
    skip_lines_at_beginning: int
    # Skip N lines at the end of the file
    skip_lines_at_end: int
    # Group results by this column
    group_by_column: [int]
    # Order results by this column, alphabetically, ascending
    order_by_column: [int]


def get_default_config() -> Config:
    return Config(',', '"', 1, 2, [5, 6, 7, 8], [0])
