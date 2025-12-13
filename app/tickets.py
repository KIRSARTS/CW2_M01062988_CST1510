import pandas as pd


def migrate_it_tickets(conn):
    data_metadata = pd.read_csv('DATA/it_tickets.csv') # 1 read data from csv
    data_metadata.to_sql('it_tickets', conn) # 3. create table, inserting the data
