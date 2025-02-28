from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# PostgreSQL Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/face_recognition_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User Table Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=False)  # Store image as binary
    encoding = db.Column(db.LargeBinary, nullable=False)    # Store face encoding as binary

# Run this only once to create tables
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
