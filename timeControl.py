import pymysql
from collections import Counter

import schedule
import time


#db_p = pymysql.connect("10.10.6.100","root","siipap_RX1","siipapx")
#db = pymysql.connect("10.10.1.225","root","sys","siipapx")
db_p =pymysql.connect("10.10.1.225","root","sys","pruebagr", charset="utf8mb4")
print("")
print("===========ONLINE=============")
print("")



def job():
    print('==================')
    try:
        print('****************')
        with db_p.cursor() as cursor:
        
            ins = "INSERT INTO `produc` (`id`, `version`,`price`) VALUES (%s, %s, %s)"
            cursor.execute(ins, ('76', '601', '100.0'))
            db_p.commit()
            print("")
            print("=================insertado correcto=====================")
            print("")

  
    except pymysql.err.IntegrityError:

        with db_p.cursor() as cursor:
            upd = " UPDATE PRODUC SET id=78,version=601,price=100.0,name=null WHERE id='78' "
            cursor.execute(upd)
            db_p.commit()
            print("")
            print("================actualizacion correcta===================")
            print("")
    



schedule.every(.1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    #time.sleep(1)

db_p.close()