from fastapi import FastAPI, UploadFile, File
from app.checker import check_file_obj
from app.database.sqlite_db import initialize_db

app = FastAPI(
    title="File Integrity Checker API",
    description="Upload a file to check if it's new, unchanged, or modified\
    based on stored hashes.",
    version="1.0.0",
)


@app.on_event("startup")
def startup_event():
    initialize_db()


@app.post("/check", summary="Check file integrity")
async def check_file(file: UploadFile = File(...)):
    """
    Upload a file to check its integrity based on stored hashes.
    """
    content = await file.read()
    print(content)
    status = check_file_obj(content)
    return {"filename": file.filename, "status": status}
