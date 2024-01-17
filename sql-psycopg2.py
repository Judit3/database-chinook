import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of database
cursor = connection.cursor()

# query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# query 2 - 
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["test"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
