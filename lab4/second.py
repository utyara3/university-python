import os
import shutil
from pathlib import Path


def unarchive(archive_path: str, dest_path: Path):
    shutil.unpack_archive(archive_path, dest_path)


def get_archive_path() -> str:
    archive_path = input("Enter path to archive: ")

    if not os.path.exists(archive_path) or not os.path.isfile(archive_path):
        exit(f"'{archive_path}' must be an existing archive!")

    return archive_path


def get_total_size_of_files(target_dir: Path) -> int:
    return sum(f.stat().st_size for f in target_dir.rglob("*") if f.is_file())


if __name__ == "__main__":
    archive_path = Path(get_archive_path())

    all_extensions = "".join(archive_path.suffixes)
    name_without_ext = Path(str(archive_path).replace(all_extensions, ""))

    unarchive(str(archive_path), name_without_ext)

    total_size_of_files = get_total_size_of_files(name_without_ext)
    print(f"Total size in archive is {total_size_of_files} bytes")

    # delete created directory
    shutil.rmtree(name_without_ext)
