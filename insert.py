import pymysql

############### CONFIGURAR ESTO ###################
# Open database connection
db = pymysql.connect("10.10.1.225","root","sys","pruebagr")
print("==coneccion establecida exitosamente==")
##################################################

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO product(id, version, price, name) \
   VALUES (3, 601, 700,'{0}')".format('html')

try:
   # Execute the SQL command
   cursor.execute(sql)
   print("*********DIOS********")
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
   print("**********ERROR***********")

# desconectar del servidor
db.close()