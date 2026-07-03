import sys
import os
import shutil

from copystatic import copy_files_recursive
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python main.py <basepath>")
        sys.exit(1)
    basepath = sys.argv[1]
    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    generate_pages_recursive("./content", "./template.html", dir_path_docs, basepath)


main()
