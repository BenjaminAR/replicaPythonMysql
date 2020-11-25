import connections
import schedule
import time
from datetime import datetime

#q="""SELECT  s.id, s.nombre, count(s.id)as TOTAL FROM traslado t join sucursal s on(t.sucursal_id=s.id) where fecha >= '2020-11-23' GROUP by s.id"""
q =  """SELECT  t.id, s.nombre FROM traslado t join sucursal s on(t.sucursal_id=s.id) where fecha >= '2020-11-23' """
        #and s.id='402880fc5e4ec411015e4ec64e70012e'

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

def  job():
    now = datetime.now()
    for i in data2:
        valor = i[0]
        name = i[1]
        if i not in data:
            q2 = "SELECT * FROM traslado where id='%s'" %valor
            connections.cenCur.execute(q2)
            mensaje = "REPLICANDO... %s" %valor
            print('*************************************************')
            print('*')
            print(mensaje,'a las' + now)
            print('*')
            print('*************************************************')
        else:
            valor = i[0]
            name = i[1]
            #print('existe----> '+ valor)
            #print('en-------->'+ name)
    print(' ')
    print('===========================================')
    print('')
    print(len(data),len(data2),name, now)
    print('')

schedule.every(.2).minutes.do(job)


while True:
    schedule.run_pending()

connections.tacuba.close()
connections.central.close()
connections.solis.close()
connections.andrade.close()
connections.bolivar.close()
connections.calle4.close()
connections.vertiz.close()
