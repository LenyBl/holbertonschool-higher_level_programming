from flask import Flask, jsonify, request
"""
Task 4: Flask API
Create a simple Flask API with the following endpoints:
- GET /: Returns a welcome message.
- GET /data: Returns a JSON object with some sample data.
- GET /status: Returns a status message.
- GET /username/<username>: Returns a JSON object with user information based
    on the provided username.
- POST /add_user: Accepts a JSON object with user information (username, name,
age, city) and adds it to an in-memory data structure. Returns a success
message with the added user information.
"""
app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    """
    Returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    """
    Returns a JSON object with some sample data.
    """
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """
    Returns a status message.
    """
    return jsonify({"status": "OK"})


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Returns a JSON object with user information based on the provided username.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Accepts a JSON object with user information (username, name, age, city) and
    adds it to an in-memory data structure. Returns a success message with the
    added user information.
    """
    new_user = request.get_json()

    if not new_user:
        return jsonify({"error": "Invalid JSON"}), 400

    username = new_user.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user_data = {
        "username": username,
        "name": new_user.get("name"),
        "age": new_user.get("age"),
        "city": new_user.get("city")
    }

    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run()
