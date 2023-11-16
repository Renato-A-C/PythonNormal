import psycopg2

conector = psycopg2.connect(host="localhost",dbname="postgres", user="postgres",password ="", port=5432)

cur = conector.cursor()
#cur.execute("""CREATE TABLE IF NOT EXISTS person (    id INT PRIMARY KEY,    name VARCHAR(255),    age INT,    gender CHAR)""")
cur.execute("""SELECT * FROM funcionario""")

for row in cur.fetchall():
    print(row)
conector.commit()
cur.close()
conector.close()


