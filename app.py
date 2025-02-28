from flask import Flask, render_template, request
from database import db, app, User
from face_recognition_utils import store_face_encoding, detect_and_compare
import base64
import os

UPLOAD_FOLDER = "static/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure upload folder exists

# Homepage - Upload Form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"].strip()
        image = request.files["image"]

        if not name or not image:
            return render_template("index.html", error="Please enter a name and upload an image.")

        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(image_path)

        success = store_face_encoding(name, image_path)
        if success:
            return render_template("index.html", message=f"Successfully added {name}!", name=name, image=image.filename)
        else:
            return render_template("index.html", error="Face not detected! Please upload a clear image.")

    return render_template("index.html")

# Video Processing Route
@app.route("/video", methods=["POST"])
def video():
    video = request.files["video"]
    if not video:
        return render_template("result.html", error="No video uploaded.")

    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(video_path)

    matched_name, snapshot_path = detect_and_compare(video_path)

    if matched_name:
        user = User.query.filter_by(name=matched_name).first()
        snapshot_encoded = base64.b64encode(open(snapshot_path, "rb").read()).decode("utf-8")

        return render_template("result.html", name=user.name, image=snapshot_encoded)
    else:
        return render_template("result.html", error="No Match Found")

if __name__ == "__main__":
    app.run(debug=True)
