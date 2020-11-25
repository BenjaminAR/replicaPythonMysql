import pymysql

db = pymysql.connect("10.10.1.225","root","sys","pruebagr")
print("==coneccion establecida exitosamente==")
# prepare a cursor object using cursor() method
cursor = db.cursor()
cursor1 = db.cursor()

# Prepare SQL query to READ a record into the database.
sql = "SELECT * FROM produc \
    WHERE id > {0}".format(0)

query = "SELECT * FROM product \
    WHERE id > {0}".format(0)

# Execute the SQL command
cursor.execute(sql)
cursor1.execute(query)

results = list(cursor.fetchall())
for row in results:
   id = row[0]
   version = row[1]
   price = row[2]
   name = row[3]
   #print ("id = {0}, version = {1}, price = {2}, name = {3}".format(id,version,price,name))
   
#print('=========================================================')


results1 = list(cursor1.fetchall())
for row1 in results1:
   id = row1[0]
   version = row1[1]
   price = row1[2]
   name = row1[3]
   #print ("id = {0}, version = {1}, price = {2}, name = {3}".format(id,version,price,name))

row = list(row)
row1 = list(row1)
results = list(results)
results1 = list(results1)
print("------------------------------------------") 
print(results) 
print("------------------------------------------")
print(results1) 



print(type(row1))
print(type(results))
print(type(results))

if results in results1:
    print("si")

else:
    print("no")

db.close()
# Desconectar del servidor

