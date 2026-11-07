import os
import shutil


def generate_test_archive():
    archive_name = "test_archive"
    source_dir = "temp_test_dir"

    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(os.path.join(source_dir, "documents"), exist_ok=True)
    os.makedirs(os.path.join(source_dir, "documents", "archived"), exist_ok=True)
    os.makedirs(os.path.join(source_dir, "images"), exist_ok=True)

    files_to_create = {
        os.path.join(source_dir, "root_file.txt"): 100,  # 100 bytes
        os.path.join(source_dir, "documents", "doc1.pdf"): 500,  # 500 bytes
        os.path.join(source_dir, "documents", "doc2.docx"): 300,  # 300 bytes
        os.path.join(source_dir, "documents", "archived", "old.txt"): 50,  # 50 bytes
        os.path.join(source_dir, "images", "avatar.png"): 650,  # 650 bytes
    }

    print("Generating files with exact sizes...")
    for file_path, size in files_to_create.items():
        with open(file_path, "wb") as f:
            f.write(b"\x00" * size)

    print(f"Archiving '{source_dir}' into '{archive_name}.zip'...")
    shutil.make_archive(archive_name, "zip", source_dir)

    print(f"Cleaning up temporary directory '{source_dir}'...")
    shutil.rmtree(source_dir)

    print(
        f"\nSuccess! '{archive_name}.zip' generated."
        f"\nExpected total size of unpacked files: 1600 bytes."
    )


if __name__ == "__main__":
    generate_test_archive()
