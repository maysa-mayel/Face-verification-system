from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
import os
from face_verification import detect_and_crop_faces, verify_face 

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})  # Allow all origins (for development)

@app.route('/verify_face', methods=['POST'])
def verify_face_endpoint():
    if 'id_image' not in request.json or 'live_image' not in request.json:
        return jsonify({"error": "Missing ID image or live image data"}), 400

    id_image_data = request.json['id_image']
    live_image_data = request.json['live_image']

    try:
        # Decode and process the ID image
        id_image = cv2.imdecode(np.frombuffer(base64.b64decode(id_image_data), np.uint8), cv2.IMREAD_COLOR)
        id_face = detect_and_crop_faces(id_image)
        if not id_face:
            return jsonify({"error": "No face detected in ID image"}), 400

        # Decode and process the live image
        live_image = cv2.imdecode(np.frombuffer(base64.b64decode(live_image_data), np.uint8), cv2.IMREAD_COLOR)
        live_face = detect_and_crop_faces(live_image)
        if not live_face:
            return jsonify({"error": "No faces detected in live image"}), 400

        # Verify the faces
        result = verify_face(id_face, live_face)
        if result['verified']:
            return jsonify({"status": "Verified"})
        else:
            return jsonify({"status": "Not Verified"})

    except Exception as e:
        return jsonify({"error": "Failed to process images"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)