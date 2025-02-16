import os
from flask import Flask, request, jsonify, send_from_directory, Response, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask_mail import Mail,Message


app = Flask(__name__, static_folder="../growSmart-frontend/dist")

app.config["SESSION_COOKIE_SECURE"] = False  # Set True if using HTTPS

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use your email provider's SMTP server
app.config['MAIL_PORT'] = 587  # Port for TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'emailsfromapp@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'jjrn meur idhg mdws'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'emailsfromapp@gmail.com'

mail = Mail(app)



# ✅ PostgreSQL Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:anuj2006@localhost/user_growSmart"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Set secret key for sessions (used to secure the session cookies)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

# ✅ User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255))  # NEW

# ✅ Plant Model
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String, nullable=False)
    soil_moisture = db.Column(db.Float, nullable=False)
    humidity_content = db.Column(db.Float, nullable=False)
    image_path = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationship to User table
    user = db.relationship('User', backref=db.backref('plants', lazy=True))

# ✅ ForumPost Model
class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.Column(db.String(100), nullable=False)  # Store username
    title = db.Column(db.Text,nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

    user = db.relationship('User', backref=db.backref('forum_posts', lazy=True))

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

    # Store user id in session (or use a token-based approach if preferred)
    session['user_id'] = user.id

    return jsonify({
        "message": "Login successful!",
        "user": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        },
    }), 200

# ✅ Fetch Plants of Logged-in User
@app.route("/api/plants", methods=["GET"])
def get_plants():
    # Check if the user is logged in
    if 'user_id' not in session:
        return jsonify({"message": "User not logged in!"}), 401

    user_id = session['user_id']

    # Fetch the plants associated with the logged-in user
    plants = Plant.query.filter_by(user_id=user_id).all()

    # Convert plants to a list of dictionaries and return them as JSON
    plants_data = [
        {
            "id": plant.id,
            "name": plant.name,
            "start_date": plant.start_date,
            "soil_moisture_content": plant.soil_moisture,
            "humidity_content": plant.humidity_content,
            "photo": plant.image_path
        }
        for plant in plants
    ]
    return jsonify(plants_data)

from flask import session, jsonify, request
from datetime import datetime

@app.route('/add_plant', methods=['POST'])
def add_plant():
    # Check if user is logged in
    user_id = session.get('user_id')  # Get user ID from the session
    if not user_id:
        return jsonify({"message": "User ID is required!"}), 400

    data = request.form  # Using `form` to handle FormData
    name = data.get('name')
    start_date = data.get('startDate')
    soil_moisture = data.get('soilMoisture')
    humidity_content = data.get('humidityContent')

    if not all([name, start_date, soil_moisture, humidity_content]):
        return jsonify({"message": "All fields are required!"}), 400

    # Handle image file upload
    image = request.files.get('image')  # Get the image file from the form
    image_path = None
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)  # Secure the filename
        image_path = filename  # Save only the filename or relative path
        image.save(image_path)  # Save the image to the upload folder

    # Save plant info to database (image_path is stored as the path in the database)
    # (Assuming you have your database models set up correctly here)
    new_plant = Plant(
        name=name,
        start_date=start_date,
        soil_moisture=soil_moisture,
        humidity_content=humidity_content,
        user_id=user_id,
        image_path=image_path  # Store the image path in the database
    )

    try:
        db.session.add(new_plant)
        db.session.commit()
        return jsonify({"message": "Plant added successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error adding plant!", "error": str(e)}), 500
    
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'uploads'), filename)


@app.route("/posts", methods=["GET"])
def get_community_posts():
    posts = ForumPost.query.order_by(ForumPost.timestamp.desc()).all()
    posts_data = [
        {
            "id": post.id,
            "username": post.username,
            "title": post.title,  # Include title in response
            "content": post.content,
            "timestamp": post.timestamp.strftime("%a, %d %b %Y %H:%M:%S")
        }
        for post in posts
    ]

    return jsonify(posts_data), 200



@app.route("/post", methods=["POST"])
def add_community_post():
    # Check if user is logged in
    user_id = session.get('user_id')  # Get user ID from the session
    if not user_id:
        return jsonify({"message": "User ID is required!"}), 400

    data = request.form  # Using `form` to handle FormData
    title = data.get('title')
    content = data.get('content')
    timestamp = data.get('timestamp')
    user = User.query.filter_by(id=user_id).first()
    new_post = ForumPost(
        title=title,
        user_id=user_id,
        content=content,
        username=user.first_name,
        timestamp=timestamp
    )

    try:
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"message": "Post added successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error adding Post!", "error": str(e)}), 500



@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        if not name or not email or not subject or not message:
            return jsonify({"error": "All fields are required"}), 400

        # Email content
        email_body = f"""
        Name: {name}
        Email: {email}
        Subject: {subject}
        
        Message:
        {message}
        """

        msg = Message(subject=f"New Contact Form Submission: {subject}",
                      recipients=['emailsfromapp@gmail.com'],  # Change this to your email
                      body=email_body)

        mail.send(msg)
        return jsonify({"success": "Message sent successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)



