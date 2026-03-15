from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host="db",
    user="root",
    password="password",
    database="usersdb"
)

cursor = db.cursor()

@app.route("/")
def home():
    return "Flask + MySQL running in Docker!"

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    name = data["name"]

    query = "INSERT INTO users (name) VALUES (%s)"
    cursor.execute(query, (name,))
    db.commit()

    return jsonify({"message": "User added"})

@app.route("/users")
def get_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    users = []
    for r in rows:
        users.append({"id": r[0], "name": r[1]})

    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)