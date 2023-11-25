from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import get_extention_text
from audio import get_text_from_audiofile
import time
import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


app = FastAPI()

origins = [
    "http://localhost:3000",
    'http://127.0.0.1:5000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/")
def home():
    return {"name": "Steve", "age": 20}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        timestamp = str(int(time.time()))
        file_name, file_extension = os.path.splitext(file.filename)
        unique_filename = f"{timestamp}_{file_name}{file_extension}"

        file_path = os.path.join("downloads/", unique_filename)

        with open(file_path, "wb") as f:
            f.write(file.file.read())

        print("File saved")

        output_file = "example.pdf"
        response_txt = handle_audio(file_path)
        create_pdf(output_file, response_txt)

        # return {"text": f"{response}"}
        # return {"text": f"File saved "}
    except Exception as e:
        print(f"Error handling file upload: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


def handle_audio(audio_path):
    user_message = get_text_from_audiofile(path=audio_path)
    return get_extention_text(user_message=user_message)['answer']

def register_russian_font():
    try:
        pdfmetrics.registerFont(TTFont("Arial", "C:/GeekBrains/geekbrains_methodist/Arial.ttf"))
    except Exception as e:
        print(f"Error registering font: {e}")


def create_pdf(file_path, text, font_name="Arial", font_size=12):
    # Register the Russian font
    register_russian_font()

    # Create the Canvas
    pdf_canvas = canvas.Canvas(file_path)

    # Set the font
    pdf_canvas.setFont(font_name, font_size)

    # Write Russian text to PDF
    pdf_canvas.drawString(100, 800, text)

    # Close the PDF file
    pdf_canvas.save()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)