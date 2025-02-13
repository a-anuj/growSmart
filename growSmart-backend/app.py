from flask import Flask, request, send_from_directory, Response, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="../growSmart-frontend/dist")
CORS(app)  # Enable CORS for all routes

@app.route("/")
def serve_vue():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    file_path = os.path.join(app.static_folder, path)

    # Ensure file exists before serving
    if os.path.exists(file_path):
        # Special handling for GIFs
        if path.endswith(".gif"):
            return Response(open(file_path, "rb").read(), mimetype="image/gif")
        return send_from_directory(app.static_folder, path)

    return "File Not Found", 404  # Return 404 if file is missing

# ✅ New Route: Handle Registration Form Submission
@app.route("/register", methods=["POST"])
def handle_registration():
    data = request.get_json()  # Get JSON data from request
    first_name = data.get("firstName", "")
    last_name = data.get("lastName", "")
    email = data.get("email", "")
    password = data.get("password", "")

    # Print the details in the terminal
    print("\n📩 New Registration Received:")
    print(f"➡️ Name: {first_name} {last_name}")
    print(f"➡️ Email: {email}")
    print(f"➡️ Password: {password}\n")  # ⚠️ Don't log passwords in real applications

    return jsonify({"message": "Registration successful!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
