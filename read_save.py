import json
from typing import Optional

from pathlib import Path

CONTENT_PATH = Path().resolve() / 'content'


def read_content(file_name: Path) -> Optional[dict]:
    path_to_file = CONTENT_PATH / file_name
    if path_to_file.exists():
        with path_to_file.open(mode='r') as file:
            return json.loads(file.read())


def save_content(file_name: Path, content: dict):
    if not CONTENT_PATH.exists():
        CONTENT_PATH.mkdir()
    path_to_file = CONTENT_PATH / file_name
    with path_to_file.open(mode='w') as customers_file_save:
        customers_file_save.write(json.dumps(content, indent=3))
