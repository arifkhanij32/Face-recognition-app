import cv2
import numpy as np
import face_recognition  # Correct module import
import pickle
import os
from database import db, User

UPLOAD_FOLDER = "static/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to store face encoding in DB
def store_face_encoding(name, image_path):
    try:
        image = face_recognition.load_image_file(image_path)  # Fix import
        encodings = face_recognition.face_encodings(image)

        if not encodings:
            print("No face detected in the image.")
            return False

        encoding = encodings[0]  # Take the first detected face
        encoded_data = pickle.dumps(encoding)  # Convert encoding to binary

        new_user = User(name=name, image_data=open(image_path, "rb").read(), encoding=encoded_data)
        db.session.add(new_user)
        db.session.commit()

        print(f"Face encoding stored for {name}")
        return True
    except Exception as e:
        print(f"Error storing face encoding: {e}")
        return False


# Function to detect and compare face from video
def detect_and_compare(video_path):
    try:
        known_encodings = {user.name: pickle.loads(user.encoding) for user in User.query.all()}
        cap = cv2.VideoCapture(video_path)
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for encoding, location in zip(face_encodings, face_locations):
                for name, stored_encoding in known_encodings.items():
                    match = face_recognition.compare_faces([stored_encoding], encoding)[0]
                    if match:
                        top, right, bottom, left = location
                        face_snapshot = frame[top:bottom, left:right]
                        snapshot_path = os.path.join(UPLOAD_FOLDER, f"_snapshot.jpg")
                        cv2.imwrite(snapshot_path, face_snapshot)

                        cap.release()
                        cv2.destroyAllWindows()
                        print(f"Match Found: {name}")
                        return name, snapshot_path  # Return matched name and snapshot path

        cap.release()
        cv2.destroyAllWindows()
        print("No Match Found")
        return None, None
    except Exception as e:
        print(f"Error during face detection: {e}")
        return None, None
