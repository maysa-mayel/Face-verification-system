# Real-Time Face Verification System

## Overview
This project is a real-time face verification system utilizing DeepFace with ArcFace for accurate face comparison. The system is designed to verify if a live face image matches a reference ID photo.
https://raw.githubusercontent.com/maysa-mayel/Face-verification-system/main/face digrame.png
## Features
- Real-time face detection and verification
- Utilizes DeepFace with ArcFace for face recognition
- API endpoint for face verification

## Requirements
- Python 3.9
- Flask (for API)
- DeepFace
- Other dependencies listed in `requirements.txt`

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the Application:**
   ```bash
   python app.py
## Usage
- **API Endpoint**: `/verify`
  - **Method**: POST
  - **Parameters**:
    - `id_image` (Base64 encoded image)
    - `live_image` (Base64 encoded image)
  - **Response**: JSON object indicating whether the images match or not.

## Folder Structure
- `faceverification.py`: Contains functions for face detection, preprocessing, and verification using DeepFace with ArcFace.
- `app.py`: Contains the Flask API for face verification.
- `requirements.txt`: Lists all dependencies.

## Contributing
Feel free to submit issues and pull requests. For significant changes, please open an issue first to discuss what you would like to change.
