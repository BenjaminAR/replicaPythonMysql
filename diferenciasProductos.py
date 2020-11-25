import pymysql

db  = pymysql.connect("10.10.5.1","root","sys","siipapx")
prod = pymysql.connect("10.10.1.229","root","sys","siipapx")
print("==coneccion establecida exitosamente==")

cursor = db.cursor()
cursor1 = prod.cursor()


sql = "SELECT * FROM producto \
     limit 1 "
    #WHERE id > {0}".format(0)

query = "SELECT * FROM producto \
     limit 1 "


cursor.execute(sql)
cursor1.execute(query)

results = cursor.fetchall()
for row in results:
   id = row[0]
   version = row[1]
   clave = row[2]
   descripcion = row[3]
   print ("id = {0}, version = {1}, price = {2}, name = {3}".format(id,version,clave,descripcion))
   
print('=========================================================')

results1 = cursor1.fetchall()
for row1 in results1:
   id = row1[0]
   version = row1[1]
   price = row1[2]
   name = row1[3]
   print ("id = {0}, version = {1}, price = {2}, name = {3}".format(id,version,price,name))

row = list(row)
row1 = list(row1)
results = list(results)
results1 =  list(results1)

 #resultados sin formato
print("------------------------------------------") 
print(results) 
print("------------------------------------------")
print(results1) 


if results == results1:
    print('coincide')
else:
   print('no coincide')
    #final_result_.pop(4)

db.close()    
prod.close()
