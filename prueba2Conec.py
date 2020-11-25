import connections

try:
    with connections.db_p.cursor() as cursor:
      
        ins = "INSERT INTO `produc` (`id`, `version`,`price`) VALUES (%s, %s, %s)"
        cursor.execute(ins, ('76', '601', '100.0'))
        connections.db_p.commit()
        print("=================insertado correcto=====================")

except connections.pymysql.err.IntegrityError:

    with connections.db_p.cursor() as cursor:
        upd = " UPDATE PRODUC SET id=78,version=601,price=100.0,name=null WHERE id='78' "
        cursor.execute(upd)
        connections.db_p.commit()
        print("================actualizacion correcta===================")


finally:
    connections.db_p.close()
