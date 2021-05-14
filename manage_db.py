import sqlite3
conn=sqlite3.connect("usersdata.db",check_same_thread=False)
c=conn.cursor()

def create_user_table():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT);')
    conn.commit()

def add_user_data(username,hashed_password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?);',(username,hashed_password))
    conn.commit()

def check_login(username,hashed_password):
    c.execute('SELECT * FROM userstable WHERE username=? AND password=?;',(username,hashed_password))
    data=c.fetchall()
    return data
    
def view_all_users():
    c.execute('SELECT * FROM userstable;')
    data=c.fetchall()
    return data