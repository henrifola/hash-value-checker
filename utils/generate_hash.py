import hashlib

def generate_bytes_hash(file_bytes: bytes, algorithm: str = "sha256") -> str:
    hash_func = getattr(hashlib, algorithm)()
    hash_func.update(file_bytes)
    return hash_func.hexdigest()