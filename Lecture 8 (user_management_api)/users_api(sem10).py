from flask import Flask, request

from repository import create_connection, get_all_users, insert_user, insert_user, delete_user

app = Flask(__name__)

DBFILE = ("D:\WebApp\G612-WebAppProgramming1-NS\Lecture 8 (user_management_api)\db\db.users")

@app.route("/api/v1/users", methods=["GET", "POST"])
def users():
    conn = create_connection("db/users.db")

    if request.method == "GET":
        users = get_all_users(conn)
        response = {
            'data': users
        }
        conn.close()
        return response, 200

    if request.method == "POST":
        user_data = request.json
        user_data = [
            user_data["username"],
            user_data["first_name"],
            user_data["last_name"],
            user_data["email"],
            user_data["password"]
        ]
        insert_user(conn, user_data)
        conn.close()
        return '', 200


@app.route("/api/v1/users/<user_id>", methods=["PUT", "DELETE"])
def updatedelete(user_id):
    conn = create_connection("db/users.db")
    #UPDATE (PUT)
    if request.method == "PUT":
        if user_id is None:
            response = {
                "Error" : "User ID input not valid, please input proper ID"
            }
            return response #reponse code?, by default da 200

    details = request.json
    if not details:
            response = {
                "Error" : "Invalid data input, input valid data"
            }
            return response #reponse code ?
    try:
        conn = connect(DBFILE)
        edit_user(conn, details=details, user_id=user_id)
        conn.close()
    except Exception as e:
            response = {
                "error": "Failed to update user. ({e})"
            }
        
            return response

    #DELETE (DELETE)
def erase_user(user_id):
    if request.method == "DELETE":
        if not user_id or user_id == "null" or user_id == "undefined":
            response = {
                "error": "--Failed to delete user. Invalid user id provided; user_id = {user_id}"
            }
            return response, 400
        try:
                conn=connect("db/users.db")
                delete_user(conn, user_id=user_id)
                conn.close()
                return "", 200
        except Exception as e:
                response = {
                    "error": f"--Failed to delete user. Error {e}"
                }
                return response, 500

    
if __name__ == "__main__":
    app.run(port=5006, debug=True)