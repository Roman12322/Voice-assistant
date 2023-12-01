from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import get_extention_text
from audio import get_text_from_audiofile

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5000",
    "http://127.0.0.1:5000",
    'http://127.0.0.1:5000/upload',
    'http://localhost:5173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/")
def home():
    return {"name": "Steve", "age": 20}


@app.post("/uploading_file")
async def upload_file(file: UploadFile = File(...)):
    try:
        print("File saved")
        return {"text": f"File saved"}
    except Exception as e:
        print(f"Error handling file upload: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

def handle_audio(audio_path):
    user_message = get_text_from_audiofile(path=audio_path)
    return get_extention_text(user_message=user_message)['answer']

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)