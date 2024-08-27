import sqlite3

# PATHS
db_path = '../data/database.db'
sql_path = 'queries.sql'

# CONNECT SQL DB
conn = sqlite3.connect(db_path)

# READ SQL FILE
with open(sql_path, 'r') as file:
    sql_query = file.read()

# EXECUTE QUERY
cursor = conn.cursor()
cursor.execute(sql_query)

# FETCH RESULTS
query_results = cursor.fetchall()

# PRINT
for row in query_results:
    print(row)

# CLOSE
conn.close()