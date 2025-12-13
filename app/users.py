





def add_user(conn, name, hash):
    curr = conn.cursor()
    sql = """ INSERT INTO users (username, password_hash) VALUES (?, ?) """
    param = (name, hash)
    curr.execute(sql,param)
    conn.commit()
    
    
    
def migrate_users(conn):
    with open('DATA/users.txt')as f:
        users = f.readlines()
        
    for user in users:
        name,hash = user.strip().split(',') 
        add_user (conn, name, hash)
    conn.close()   
    