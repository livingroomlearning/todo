import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="todo",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS todos;')
cur.execute('CREATE TABLE todos (id serial PRIMARY KEY,'
                                 'goal varchar (150) NOT NULL);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO todos (goal)'
            'VALUES (%s)',
            ('Get a working app put together',)
            )


cur.execute('INSERT INTO todos (goal)'
            'VALUES (%s)',
            ('Deploy the app to the internet',)
            )

conn.commit()

cur.close()
conn.close()