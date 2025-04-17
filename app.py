from flask import Flask, render_template, request, jsonify
import whisper
import tempfile
import os

app = Flask(__name__)

# Load the Whisper model (using the 'base' or 'medium' model; change as needed)
model = whisper.load_model("base")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Retrieve the audio file from the request
    audio = request.files.get('audio')
    if not audio:
        return jsonify({"error": "No audio file provided"}), 400

    # Save audio to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        audio.save(temp_audio.name)
        temp_filename = temp_audio.name

    try:
        # Transcribe the audio file using Whisper
        result = model.transcribe(temp_filename)
        transcription = result.get("text", "Transcription failed.")
    except Exception as e:
        transcription = f"Error during transcription: {str(e)}"
    finally:
        os.remove(temp_filename)

    return jsonify({"transcription": transcription})

if __name__ == '__main__':
    app.run(debug=True)
