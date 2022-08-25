import json
from os import mkdir
from typing import Optional

from pathlib import Path


def read_content(path_to_file: Path) -> Optional[dict]:
    if path_to_file.exists():
        with path_to_file.open(mode='r') as file:
            return json.loads(file.read())
    else:
        Path('content').mkdir()
        return []


def save_content(path_to_file: Path, new_record: dict):
    current_obj = read_content(path_to_file)
    current_obj.append(new_record)
    with path_to_file.open(mode='w') as customers_file_save:
        customers_file_save.write(json.dumps(current_obj, indent=3))
