# python app.py >> /tmp/info.log 2>> /tmp/error.log
from flask import Flask, jsonify, request
from flask_cors import CORS

# from model import get_extention_text
# from audio import get_text_from_audiofile
import time
import os

app = Flask(__name__)
CORS(app)

app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024


@app.route("/")
def home():
    return jsonify({"name": "Steve", "age": 20})


@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        file = request.files["file"]

        timestamp = str(int(time.time()))
        file_name, file_extension = os.path.splitext(file.filename)
        unique_filename = f"{timestamp}_{file_name}{file_extension}"

        file_path = os.path.join("downloads/", unique_filename)

        file.save(file_path)
        print("File saved")

        # response = handle_audio(file_path)

        return jsonify({"message": f"File {unique_filename} saved successfully"}), 200
        # return jsonify({"text": f"{response}"}), 200
    except Exception as e:
        print(f"Error handling file upload: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


# def handle_audio(audio_path):
#     user_message = get_text_from_audiofile(path=audio_path)
#     return get_extention_text(user_message=user_message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
