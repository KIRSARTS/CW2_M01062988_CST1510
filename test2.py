import sqlite3
import pandas as pd


def create_user_table():
    curr = conn.cursor()

    sql = """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
    ) """
    
def add_user(conn, name, password):
    curr = conn.cursor()
    sql = """ INSERT INTO users (username, password_hash) VALUES (?, ?) """
    param = (name, password)
    curr.execute(sql,param)
    conn.commit()



def migrate_users(conn):
    with open('DATA/users.txt')as f:
        users = f.readlines()
        
    for user in users:
        name,hash = user.strip().split(',') 
        add_user (conn, name, hash)
    conn.close() 


#conn = sqlite3.connect('DATA/intelligence_platform.db')


def migrate_cyber_incidents():
    cyber = pd.read_csv('DATA/cyber_incidents.csv')
    #print(cyber.head(5))
    conn = sqlite3.connect('DATA/intelligence_platform.db')
    cyber.to_sql('cyber_incidents', conn, if_exists = 'append', index = False)
    print('Migrated all cyber_incidents')
    
def read_all_cyber_incidents_pandas():
    conn = sqlite3.connect('DATA/intelligence_platform.db')
    query = "SELECT * FROM cyber_incidents"
    cyber_table = pd.read_sql(query, conn)
    print(cyber_table.head(5))
    
    
def migrate_datasets_metadata(conn):
    data_metadata = pd.read_csv('DATA/datasets_metadata.csv') # 1 read data from csv
    data_metadata.to_sql('datasets_metadata', conn) # 3. create table, inserting the data
   

def migrate_it_tickets(conn):
    data_metadata = pd.read_csv('DATA/it_tickets.csv') # 1 read data from csv
    data_metadata.to_sql('it_tickets', conn) # 3. create table, inserting the data




def get_all_datasets_metadata(conn):
    sql = 'SELECT * FROM datasets_metadata'
    data = pd.read_sql(sql, conn)
    conn.close()
    return data

conn = sqlite3.connect('DATA/intelligence_platform.db') # 2. create connection

conn.close()
