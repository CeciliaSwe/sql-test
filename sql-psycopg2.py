import psycopg2

# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database - like array in JS
# anything queried in database will become part of the cursor object
# which we can iterate over with a for loop
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')


# fetch the results (multiple)
results = cursor.fetchall()

# fetch result single
# results = cursor.fetchone()

# close connection
connection.close()

# print results
for result in results:
    print(result)

