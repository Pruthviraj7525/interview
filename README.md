"# interview" 
Q import small dataset using roboflow.
Solution : 
import roboflow

rf = roboflow.Roboflow(api_key=YOUR_API_KEY_HERE)
workspace = rf.workspace("WORKSPACE_URL")
workspace.upload_dataset(
    
    num_workers=10,
    project_license="Interview",
    project_type="object-detection",
    batch_name=None,
    num_retries=0
)

Q : extracts frames from given video using opencv and pytorch.
Solution :

import cv2
import os

cam = cv2.VideoCapture("video.avi")

frameno = 0
while(True):
   ret,frame = cam.read()
   if ret:
      # if video is still left continue creating images
      name = str(frameno) + '.jpg'
      print ('new frame captured...' + name)

      cv2.imwrite(name, frame)
      frameno += 1
   else:
      break

cam.release()
cv2.destroyAllWindows()

Q : connects postgressSQL and retrieve data from table 
Solution :

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



"# interview" 
"# interview" 
