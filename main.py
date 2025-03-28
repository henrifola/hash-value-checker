import sys
from app.database.sqlite_db import initialize_db
from app.checker import check_file_obj


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <filename>")
        sys.exit(1)

    # For testing, we still read the file from a path
    identifier = sys.argv[1]
    with open(identifier, "rb") as f:
        file_bytes = f.read()

    status = check_file_obj(identifier, file_bytes)
    print(f"File '{identifier}' status: {status}")


if __name__ == "__main__":
    initialize_db()
    main()
