# File Integrity Checker

## Overview
This project provides a File Integrity Checker API to verify whether a file has been modified or is unchanged. It uses hashing to compare file contents by generating unique hashes and storing them in an SQLite database.

## Features
- Upload a file and compare its contents against a stored hash to check if it’s new, modified, or unchanged.

- Uses SHA-256 hashing for file comparison.

- Supports API access via FastAPI.

- Stores file integrity hashes and paths in an SQLite database.

- Automatically tracks changes to files based on their path and hash

## Setup Instructions
* Prerequisites
Python 3.8+ is required.

    Install dependencies from requirements.txt:
    ```
    pip install -r requirements.txt
    ```
* Running the API
    * To start the FastAPI server, run the following command:
    ```
    uvicorn api:app --reload
    ```
    * Docs at
    ```
    http://127.0.0.1:8000/docs
    ```
* Running the CLI Script
    python3 main.py <filepath>

## Setup Pre-commit Hooks
To ensure code is formatted and linted before committing, install the pre-commit hooks by running:
```
pre-commit install
```

## Directory Structure
```
HASH-VALUE/
├── api.py                  # FastAPI entry point
├── main.py                 # CLI entry point
│
├── app/                    # Application logic
│   ├── __init__.py
│   ├── checker.py
│   ├── storage/            # Persistent storage (hash database)
│   │   └── hash_store.db           
│   └── database/
│       ├── __init__.py
│       └── sqlite_db.py
│
├── utils/                  # Helper modules
│   ├── __init__.py
│   ├── compare_hashes.py
│   └── generate_hash.py
│
├── requirements.txt        # Dependency list
└── README.md               # Project documentation
```
## Database
The SQLite database stores hash of each file. There is an incremental PK, and the hash is updated when the file changes.

The storage/hash_store.db file will contain the database.
