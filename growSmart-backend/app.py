import os
from flask import Flask, request, jsonify, send_from_directory, Response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder="../growSmart-frontend/dist")

# ✅ PostgreSQL Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:anuj2006@localhost/user_growSmart"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ✅ User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255))  # NEW

# ✅ Create Database Tables (Run Once)
with app.app_context():
    db.create_all()

# ✅ Serve Vue App
@app.route("/")
def serve_vue():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    file_path = os.path.join(app.static_folder, path)

    if os.path.exists(file_path):
        if path.endswith(".gif"):
            return Response(open(file_path, "rb").read(), mimetype="image/gif")
        return send_from_directory(app.static_folder, path)

    return "File Not Found", 404

# ✅ Register User
@app.route("/register", methods=["POST"])
def handle_registration():
    data = request.get_json()
    
    first_name = data.get("firstName", "").strip()
    last_name = data.get("lastName", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "").strip()

    if not first_name or not last_name or not email or not password:
        return jsonify({"message": "All fields are required!"}), 400

    # Check if user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "User already exists!"}), 400

    # Hash the password before storing it
    hashed_password = generate_password_hash(password)

    # Save new user to the database
    new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Registration successful!"}), 201

# ✅ Login User and Fetch Plants
@app.route("/login", methods=["POST"])
def handle_login():
    data = request.get_json()
    
    email = data.get("email", "").strip()
    password = data.get("password", "").strip()

    # Check if user exists
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials!"}), 401

    return jsonify({
        "message": "Login successful!",
        "user": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        },
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
