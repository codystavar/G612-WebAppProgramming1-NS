import sqlite3

# connect to db --> connection object
def create_connection(conn):
    conn = sqlite3.connect('D:/WebApp/G612-WebAppProgramming1-NS/user_management_api/users.db')
    return conn


# get all data inside the users table
def get_all_users(conn):
        query = "SELECT * FROM users"
        cursor = conn.cursor()
        data = list(cursor.execute(query))
        return data

def get_user_email_and_pass(conn, username):
        query = f"""SELECT username, email, password FROM users WHERE username = '{username}'"""
        cursor = conn.cursor()
        results = list(cursor.execute(query))
        return results[0]


def insert_user(conn, user_data):
#insert into users (username, first_name, last_name, email, password)
#values (?, ?, ?, ?, ?)
    #manual add
    query = """ INSERT INTO users (username, first_name, last_name, email, password, id, created_at, last_updated_at, last_signed_in) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor = conn.cursor()
    cursor.execute(query, user_data)
    conn.commit() #fara commit, nu se baga in baza de date
    cursor.close()



#def delete_user(conn):
#insert into users (username, first_name, last_name, email, password)
#values (?, ?, ?, ?, ?)
    #manual add
    #query = """ DELETE FROM users (username, first_name, last_name, email, password) VALUES (?,?,?,?,?);"""
    #user = ('username3', 'n', 'S', 'b@#what.com', 'password[lol]')
    #cursor.execute(query, user)
    #conn.commit() #fara commit, nu se baga in baza de date
