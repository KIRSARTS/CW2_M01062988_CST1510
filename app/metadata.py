
import pandas as pd

def migrate_datasets_metadata(conn):
    data_metadata = pd.read_csv('DATA/datasets_metadata.csv') # 1 read data from csv
    data_metadata.to_sql('datasets_metadata', conn) # 3. create table, inserting the data
    

def get_all_datasets_metadata(conn):
    sql = 'SELECT * FROM datasets_metadata'
    data = pd.read_sql(sql, conn)
    conn.close()
    return data 
    
    