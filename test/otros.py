import pymysql
from collections import Counter


db_p = pymysql.connect("10.10.6.100","root","siipap_RX1","siipapx")
#db = pymysql.connect("10.10.1.225","root","sys","siipapx")
#db_p =pymysql.connect("10.10.1.225","root","sys","pruebagr", charset="utf8mb4")
print("")
print("===========ONLINE=============")
print("")


#10.10.7.100 solis  ---> 5.6    CONECTA
#10.10.2.1          ---> 5.1    CONECTA
#10.10.4.1          ---> 5.1    CONECTA            BOLIVAR
#10.10.5.1          ---> 5.1    CONECTA
#10.10.1.101        ---> 5.1    CONECTA
#10.10.6.100        ---> 8.0    CONECTA
#10.10.1.225        ---> 5.0    CONECTA


cursor= db_p.cursor()
cursor2 = db_p.cursor()

q = """SELECT * FROM SUCURSAL WHERE NOMBRE= %s"""
q_p="""SELECT * FROM SUCURSAL WHERE NOMBRE= %s """
'''
query = """select * from db where name like 'Al%%' and date = %s"""
cursor.execute(query, ('2015_05_21', ))
'''

#cursor.execute(q)
cursor2.execute(q_p,'TACUBA')
cursor.execute(q,'TACUBA')

data = cursor2.fetchall()
data2 = cursor.fetchall()
print(data)
print(data2)
print(type(data))
print( len(data) )
print(len(data2))

db_p.close()