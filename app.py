from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
from PIL import Image
import io
import os # Import os to get environment variable

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    print("FastAPI application is starting up...")
    # Optional: Print the port it's trying to bind to
    print(f"Attempting to bind on port: {os.environ.get('PORT')}")


@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    input_data = await file.read()
    output_data = remove(input_data)
    return {
        "filename": file.filename,
        "image": output_data.hex()
    }
