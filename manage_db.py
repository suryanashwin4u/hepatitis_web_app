import sqlite3
conn=sqlite3.connect("usersdata.db",check_same_thread=False)
c=conn.cursor()

def create_table_db():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT);')
    conn.commit()

def add_user_db(new_username,hashed_password):

    c.execute('SELECT * FROM userstable WHERE username=? AND password=?;',(new_username,hashed_password))
    data=c.fetchall()
    if data:
        return "user already exists, please go to login form and start your session"
    else:
        c.execute('INSERT INTO userstable(username,password) VALUES (?,?);',(new_username,hashed_password))
        conn.commit()
        

def check_login(get_username,hashed_password):
    c.execute('SELECT * FROM userstable WHERE username=? AND password=?;',(get_username,hashed_password))
    data=c.fetchall()
    return data
    
def view_all_users():
    c.execute('SELECT * FROM userstable;')
    data=c.fetchall()
    return data