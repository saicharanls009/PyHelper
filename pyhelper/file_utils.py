
from pathlib import Path
import shutil


def write_file(file_path, content):
    path = Path(file_path)
    path.write_text(content, encoding="utf-8")
    return True


def read_file(file_path):
    path = Path(file_path)
    return path.read_text(encoding="utf-8")


def copy_file(source, destination):
    shutil.copy2(source, destination)
    return True


def file_extension(file_path):
    return Path(file_path).suffix


def file_exists(file_path):
    return Path(file_path).is_file()


def file_size(file_path):
    return Path(file_path).stat().st_size


def count_lines(file_path):
    content = read_file(file_path)
    if not content:
        return 0
    return len(content.splitlines())
