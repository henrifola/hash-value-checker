from utils.generate_hash import generate_bytes_hash
from app.database.sqlite_db import check_for_hash, insert_or_update_hash


def check_file_obj(file_bytes: bytes) -> str:
    file_hash = generate_bytes_hash(file_bytes)
    existing_hash = check_for_hash(file_hash)

    if existing_hash:
        print("Hash exists")
        return "Hash value already exists"
    else:
        print("New hash value")
        insert_or_update_hash(file_hash)
        return "New hash value"
