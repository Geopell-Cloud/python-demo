from fastapi import FastAPI, UploadFile, File
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"
BACKUP_FOLDER = "backup"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(BACKUP_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "FastAPI File Service is running"}

@app.get("/hello")
def hello():
    return {"message": "Hello Message from FastAPI"}
    
@app.get("/product")
def product():
    #return {"message": "Give me the product list from FastAPI"}
    

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):

    # Save uploaded file
    upload_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Copy file to backup folder
    backup_path = os.path.join(BACKUP_FOLDER, file.filename)
    shutil.copy2(upload_path, backup_path)

    return {
        "message": "File uploaded and copied successfully",
        "filename": file.filename,
        "upload_location": upload_path,
        "backup_location": backup_path
    }
