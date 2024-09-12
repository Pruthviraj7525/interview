
import psycopg2

# establishing the connection
conn = psycopg2.connect(
database="test",
	user='postgres',
	password='password',
	host='localhost',
	port= '5432'
)

# Creating a cursor object using the cursor()
# method
cursor = conn.cursor()

sql = '''CREATE TABLE VIDEO_ANALYSIS(
FRAME_ID BIGSERIAL NOT NULL PRIMARY KEY,
OBJECT_DETACTED BYTEA NOT NULL,
TIMESTAMP TIMESTAMP(6) NOT NULL 
)'''
cursor.execute(sql)

# Display whole table
cursor.execute("SELECT * FROM VIDEO_ANALYSIS ")
print(cursor.fetchall())

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
