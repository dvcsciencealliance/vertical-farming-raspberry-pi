import pyodbc
import psycopg2
import datetime

timeFormat = '%Y-%m-%d %H:%M:%S'

now = datetime.datetime.now()

fin = open('config/db.cfg')
username = fin.readline().rstrip()
password = fin.readline().rstrip()
host = fin.readline().rstrip()
databasename = fin.readline().rstrip()

#cnxn = pyodbc.connect('DRIVER={psycopg2};SERVER=' + host + ';DATABASE=' + databasename + ';UID=' + username + ';PWD=' + password)

conn = psycopg2.connect(host = host, user = username, password = password, dbname = databasename)
cur = conn.cursor()


# Execute a command: this creates a new table
#cur.execute("CREATE TABLE Arduino1 (id serial PRIMARY KEY, time TIMESTAMP, thermistor1 float, phSensor1 float);")
#cur.execute("DROP TABLE Arduino1;")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
#cur.execute("INSERT INTO Thermistor1 (data, time) VALUES (%s, %s)", (13.2, now.strftime(timeFormat)))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM Arduino1;")
print(cur.fetchall())


# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn=conn.close()
