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
          
          
def get_all_cyber_incidents(conn):
    sql = 'SELECT * FROM cyber_incidents'
    data = pd.read_sql(sql, conn)
    conn.close()
    return data          