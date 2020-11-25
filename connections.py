import pymysql

central = pymysql.connect("10.10.1.229","root","sys","siipapx")
solis = pymysql.connect("10.10.7.100","root","sys","siipapx")
andrade = pymysql.connect("10.10.2.1","root","sys","siipapx")
bolivar = pymysql.connect("10.10.4.1","root","sys","siipapx")
calle4 = pymysql.connect("10.10.5.1","root","sys","siipapx")
tacuba = pymysql.connect("10.10.1.101","root","sys","siipapx")
vertiz = pymysql.connect("10.10.6.100","root","siipap_RX1","siipapx")


db_p =pymysql.connect("10.10.1.225","root","sys","pruebagr")

print("")
print("===========ONLINE=============")
print("")

solCur = solis.cursor()
andCur = andrade.cursor()
bolCur = bolivar.cursor()
ca4Cur = calle4.cursor()
tacCur = tacuba.cursor()
verCur = vertiz.cursor()
cenCur = central.cursor()

q="""SELECT ID,ACTIVA, SERVER FROM data_source_replica WHERE ACTIVA=true"""

cenCur.execute(q)

data = cenCur.fetchall()

activo = b'\x01'
inActi = b'\x00'


for i in data:
    iD = i[0]
    Activo = i[1]
    name = i[2]
    #compro = activo == Activo
    #print(compro)
    if  Activo == activo:
        q2 = "SELECT * FROM data_source_replica where id='%s'" %iD
        mensaje = "REPLICANDO... %s" %iD
        print(mensaje)
  
    else:
        print('algo mal')