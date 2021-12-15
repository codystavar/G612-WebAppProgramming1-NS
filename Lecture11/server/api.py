from flask import Flask, request
from flask_cors import CORS
from werkzeug.wrappers import response
from Lecture11.database.repository import get_connection, create_user, get_email_and_password

app = Flask ("myfirstusermanagementapp")

CORS(app)

DB_FILE = '../database/users.db'

@app.route('/api/v1/users', methods=["POST"])
def users():
    user_details = request.json
    try:
        conn = get_connection(DB_FILE)
        create_user(conn, user_details)
        conn.close()
        return '', 200
    except Exception as e:
        error = {
            'error': {e}
        }
        return e, 500



@app.route('/api/v1/users/<email>', methods=["GET"])
def get_users(email):
    if email is None:
        error = {
            "error": "Invalid email provided."
        }
        return error, 400

    try:
        conn = get_connection(DB_FILE)
        user = get_email_and_password(conn, email)
        response = {
            "user" : user
        }
        return response, 200
    except Exception as e:
        error = {
            "error": f"-- Failed to fetch user. {e}"
        }
        return error, 500

@app.route('api/v1/sign-in', methods=["POST"])
def sign_in():
    body = request.json
    email = body.get("email", None)
    password = body.get("password", None)
    if email is None:
        error = {
            "error": "--Please provide an email."
        }
        return error, 400

    if password is None:
        error = {
            "error": "--Please provide a password."
        }
        return error, 400

    #sign in
    try:
        conn = get_connection(DB_FILE)
        user = get_email_and_password(conn, email)
        if user and user["password"] == password:
            return '', 204
        else:
            error = {
                "error": "--Failed to sign in. Email or password are invalid"
            }
            return error, 401

    except Exception as e:
        error = {
            "error": f"--Failed to sign in. {e}"
        }
        return error, 500

if __name__ == "__main__":
    app.run(debug=True, port=3005)