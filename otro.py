import pymysql


db = pymysql.connect("10.10.6.100","root","siipap_RX1","siipapx")
#print("conexion vertiz")
#db = pymysql.connect("10.10.7.1","root","sys","siipapx")
print("conexion otra")


#cursor = db.cursor()
cursor = db.cursor()

sql = "SELECT * FROM sucursal \
WHERE id > {0}".format(0)

#cursor.execute(sql)
cursor.execute(sql)

#result = cursor.fetchall()
result = cursor.fetchall() 

final_result = [list(i) for i in result]

#print(result)
print(final_result)
'''
final_result = [list(i) for i in result]
final_result_ = [list(i) for i in result_]

#print(final_result)
#print('============================================================================================')
#print(final_result_)

result = map(lambda x, y: x == y, final_result, final_result_) 
print(list(result)) 
'''
'''
def comparar_listas(final_result, final_result_):
    return Counter(final_result) == Counter(final_result_)

print(comparar_listas(result, result_))
#print(comparar_listas(numeros_2, numeros_3))
#print(comparar_listas(numeros_1, numeros_3))
'''
#db.close()    
db.close()
'''
dicc = {12345: 'Luggage Combination', 42: 'The Answer'}

print(type(dicc))

print(dicc)
'''
