
from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Ali", "major": "Software"},
    {"id": 2, "name": "Sara", "major": "IT"}
]

tasks = [
    {"id": 1, "title": "Programming Assignment", "completed": False},
    {"id": 2, "title": "Database Project", "completed": True}
]


@app.route("/")
def home():
    return jsonify({"message": "College Management System API is running!"})


@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200


@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    user = {
        "id": max([u["id"] for u in users], default=0) + 1,
        "name": data["name"],
        "major": data.get("major", "Unknown")
    }
    users.append(user)
    return jsonify(user), 201


@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json() or {}
    user.update({k: data[k] for k in ("name", "major") if k in data})
    return jsonify(user), 200


@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    users.remove(user)
    return "", 204


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200


@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    task = {
        "id": max([t["id"] for t in tasks], default=0) + 1,
        "title": data["title"],
        "completed": False
    }
    tasks.append(task)
    return jsonify(task), 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json() or {}
    task.update({k: data[k] for k in ("title", "completed") if k in data})
    return jsonify(task), 200


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    tasks.remove(task)
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
