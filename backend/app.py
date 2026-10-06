from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# Configure these values through environment variables.
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "YOUR_RDS_ENDPOINT"),
    "user": os.getenv("DB_USER", "YOUR_DB_USER"),
    "password": os.getenv("DB_PASSWORD", "YOUR_DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "dev"),
    "port": int(os.getenv("DB_PORT", "3306"))
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route("/")
def index():
    return "AWS Three-Tier Web Application - Flask Backend"

@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users ORDER BY id")
        return jsonify(cursor.fetchall())
    finally:
        cursor.close()
        conn.close()

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        if user:
            return jsonify(user)
        return jsonify({"error": "User not found"}), 404
    finally:
        cursor.close()
        conn.close()

@app.route("/users/add", methods=["POST"])
def add_user():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and Email are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()
        return jsonify({"message": "User added successfully"}), 201
    except mysql.connector.Error as err:
        conn.rollback()
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route("/users/update/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and Email are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE users SET name = %s, email = %s WHERE id = %s",
            (name, email, user_id)
        )

        if cursor.rowcount == 0:
            conn.rollback()
            return jsonify({"error": "User not found"}), 404

        conn.commit()
        return jsonify({"message": "User updated successfully"})
    except mysql.connector.Error as err:
        conn.rollback()
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route("/users/delete/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))

        if cursor.rowcount == 0:
            conn.rollback()
            return jsonify({"error": "User not found"}), 404

        conn.commit()
        return jsonify({"message": "User deleted successfully"})
    except mysql.connector.Error as err:
        conn.rollback()
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
