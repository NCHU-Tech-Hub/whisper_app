
> **Note:** The `.idx/dev.nix` file in this repo is only used by [Firebase Studio](https://firebase.google.com/docs/studio/customize-workspace) to configure the development environment

---

## Overview

This project is a simple web application built with Flask that leverages OpenAI’s Whisper model for speech‑to‑text transcription. Users can upload audio files (e.g., WAV, MP3) through a browser interface and receive back accurate, timestamped transcriptions in multiple languages citeturn4search0turn5search1.

## Features

- **Easy Audio Upload**  
  Drag-and-drop or select audio files to transcribe.
- **Multilingual Recognition**  
  Whisper supports transcription in 90+ languages citeturn5search1.
- **Streaming Support** *(optional)*  
  For longer files, transcription is streamed in 30 s windows citeturn5search0.
- **JSON & Plain Text Output**  
  Download transcriptions as structured JSON or plain `.txt`.
- **Customizable Frontend**  
  Edit the HTML/CSS under `templates/` and `static/` for your own styling.

## Prerequisites

- **Python 3.9+**  
- **pip** (Python package manager)  
- **ffmpeg** (for certain audio formats)  
- **Virtual Environment** (recommended)

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/NCHU-Tech-Hub/whisper_app.git
   cd whisper_app
   ```
2. **Create and activate a virtual environment**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install Python dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
   This will pull in Flask, `whisper`, and other needed libraries citeturn4search4.

## Usage

1. **Start the Flask development server**  
   ```bash
   export FLASK_APP=app.py
   flask run
   ```

## Configuration

- **Model Selection**  
  In `app.py`, change  
  ```python
  model = whisper.load_model("base")
  ```  
  to `"small"`, `"medium"`, or `"large"` to trade off speed vs. accuracy
- **Environment Settings**  
  The included `.idx/dev.nix` file is only for Firebase Studio workspace setup—see the [Firebase Studio guide](https://firebase.google.com/docs/studio/customize-workspace) 


