import connections

#q="""SELECT  s.id, s.nombre, count(s.id)as TOTAL FROM traslado t join sucursal s on(t.sucursal_id=s.id) where fecha >= '2020-11-23' GROUP by s.id"""
q =  """SELECT  t.id, s.nombre FROM traslado t join sucursal s on(t.sucursal_id=s.id) where fecha >= '2020-11-23' and s.id='402880fc5e4ec411015e4ec64e70012e'"""


#q= "select * from SUCURSAL where nombre='tacuba'"
uno = 'el registro existe '
connections.cenCur.execute(q)
connections.tacCur.execute(q)

data = connections.cenCur.fetchall()
data2 = connections.tacCur.fetchall()


comp = set(data2) - set(data)


'''
for i in comp:
    valor = i[0]
    q2 = "SELECT * FROM traslado where id='%s'" %valor
    print(q2)
'''     



for i in data2:
    if i not in data:
        valor = i[0]
        q2 = "SELECT * FROM traslado where id='%s'" %valor
        mensaje = "REPLICANDO... "
        print(q2)
    
    else:
        valor = i[0]
        print('existe----> '+ valor)


#print(data)
#print('=======================================================================================')
#print(data2)

#print(final_result)
#print (final_result.difference(final_result2))

'''



for index, item in enumerate(data[0]):
    try:     
        data2[0].index(item)
        print('igual')
    except:
        print('')
        print('el valor del item no se encuentra ')
        print(item)
        print('')
        #q2 = "SELECT id FROM traslado where id='%s'" %item
        #print(q2)
'''
print('')
print(len(data))
print(len(data2))
   

connections.tacuba.close()
connections.central.close()
connections.solis.close()
connections.andrade.close()
connections.bolivar.close()
connections.calle4.close()
connections.vertiz.close()



#pymysql.err.ProgrammingError: #ERROR EN LA QUERY
