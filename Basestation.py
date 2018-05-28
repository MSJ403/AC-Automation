import MySQLdb
import time,serial 

def Update():
# Open database connection
        db = MySQLdb.connect(host=" ", user=" ", passwd=" ", db=" ") 
# prepare a cursor object using cursor() method
        cursor = db.cursor()
# Prepare SQL query to UPDATE required records
        sql = "UPDATE temp SET Flag = '0' WHERE ID = '1'"
        try:
           # Execute the SQL command
            cursor.execute(sql) 
           # Commit your changes in the database
            db.commit() 
        except:
           # Rollback in case there is any error
            db.rollback()
        db.close()
# disconnect from server

# Open Serial to Communicate with the Xbee       
ser = serial.Serial("/dev/ttyUSB0" , 9600 ,timeout = None)
ser.isOpen()

count = 1

##Iterate 
while (count > 0 ): 
  # Open database connection
  db = MySQLdb.connect(host=" ", user=" ", passwd=" ", db=" ")
  #create a cursor for the select
  cur = db.cursor()
  #execute an sql query
  cur.execute("SELECT * FROM temp")
  for row in cur:  # print all the first cell of all the rows
    flag = str(row[3]) # Check the flag 
    if flag == '1':
        Update() 
        x = str(row[1])
        print x
        ##print
        y = x.encode('ascii')
        ser.write(bytes(y)) # Send the AC signal through Xbee
    else:
      count +=1
    count +=1
count +=1
