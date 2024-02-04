from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from docx import Document
from tempfile import NamedTemporaryFile
import shutil

app = FastAPI()

# Set up CORS middleware options
origins = [
    "http://localhost:5173",  # Vue.js server
    "http://127.0.0.1:5173",  # Alternative Vue.js server
    # Add other domains/ports as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # Temporary file to store uploaded .docx
    with NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        temp_file_path = temp_file.name
    
    # Process the file to capitalize all text
    doc = Document(temp_file_path)
    for paragraph in doc.paragraphs:
        paragraph.text = paragraph.text.upper()

    # Save the modified file
    new_file_path = temp_file_path.replace(".docx", "_CAPITALIZED.docx")
    doc.save(new_file_path)

    # Return the new file to the user
    return FileResponse(path=new_file_path, filename=file.filename.replace(".docx", "_CAPITALIZED.docx"), media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
