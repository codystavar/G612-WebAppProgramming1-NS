#db + repository + API
import sqlite3

def get_connection(dbfile):
    try:
        conn = sqlite3.connect(dbfile)
        return conn
    except Exception as e:
        raise 

def get_email_and_password(conn, email=None):
    query = f"""select email, password, from users where email = '{email}'"""
    try:
        cursor = conn.cursor()
        user = list(cursor.execute(query))
        if len(user):
            # user = user[0]
            user = {
                "email": user[0][0],
                "password": user[0][1] #elementul 0, info 1
            }
            return user
    except Exception as e:
        raise e

def create_user(conn, user_details):
    query ="""insert into users (name, email, password)
        values (?, ?, ?)"""
    try:
        cursor = conn.cursor()
        cursor.execute(query, user_details)
        conn.commit()
    
    except Exception as e:
        raise Exception(f"--Failed to create user with details")