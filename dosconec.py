import pymysql
from collections import Counter


#db_p = pymysql.connect("10.10.6.100","root","siipap_RX1","siipapx")
#db = pymysql.connect("10.10.1.225","root","sys","siipapx")
db_p =pymysql.connect("10.10.1.225","root","sys","pruebagr", charset="utf8mb4")
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

q = "SELECT * FROM PRODUCT"
q_p="SELECT * FROM PRODUC "

#cursor.execute(q)
cursor2.execute(q_p)
cursor.execute(q)

data = cursor2.fetchall()
data2 = cursor.fetchall()
print(data)
print(data2)
print(type(data))
print( len(data) )
print(len(data2))


def comp_reg(a, b):
    return a in b

print(comp_reg(cursor, cursor2))


if data in data2:
    print("si")

else:
    print("no-------")
    #ins = "INSERT INTO `produc` (`id`, `version`,`price`) VALUES (%s, %s, %s)"
    #cursor.execute(ins, ('78', '601', '100.0'))
    #connection.commit()


try:
    with db_p.cursor() as cursor:
      
        ins = "INSERT INTO `produc` (`id`, `version`,`price`) VALUES (%s, %s, %s)"
        cursor.execute(ins, ('76', '601', '100.0'))
        db_p.commit()
        print("=================insertado correcto=====================")

    with db_p.cursor() as cursor:
        
        consulta = "SELECT * FROM PRODUC"
        cursor.execute(consulta)
        result = cursor.fetchall()
        print(result)

except pymysql.err.IntegrityError:

    with db_p.cursor() as cursor:
        upd = " UPDATE PRODUC SET id=78,version=601,price=100.0,name=null WHERE id='78' "
        cursor.execute(upd)
        db_p.commit()
        print("================actualizacion correcta===================")

finally:
    db_p.close()



       
       
    #ins='INSERT INTO PRODUC (id,version,price) VALUES (78,601,100.0)'
    #cursor.execute(ins)
