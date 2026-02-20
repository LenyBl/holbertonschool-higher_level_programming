from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/data", methods=['GET'])
def data():
    """
    Returns a JSON object with some sample data.
    :return: A JSON object containing sample data.
    """
    return jsonify(users)


@app.route("/status", methods=['GET'])
def status():
    """
    Returns a status message.
    :return: A JSON object containing the status message.
    """
    return jsonify({"status": "OK"})


@app.route("/username/<username>", methods=['GET'])
def getUsername(username):
    """
    Returns a JSON object with user information based on the provided username.
    """
    user_info = users.get(username)
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def addUser():
    """
    Accepts a JSON object with user information and adds it to the existing
    data.
    Returns a success message upon successful addition.
     :return: A JSON object containing a success message or an error message if
     the input is invalid or the user already exists.
    """
    if request.method == 'POST':
        new_user = request.get_json()
        if "username" not in new_user:
            return jsonify(error="Invalid JSON"), 400
        username = new_user["username"]
        if username in users:
            return jsonify(error="User already exists"), 409
        users[username] = {
            "name": new_user.get("name", ""),
            "age": new_user.get("age", 0),
            "city": new_user.get("city", "")
        }
        return jsonify({"message": "User added successfully"}), 201


if __name__ == "__main__":
    app.run()
