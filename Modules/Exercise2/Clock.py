from os import system
import time
import datetime
import locale

locale.setlocale(locale.LC_ALL, "es-mx") #Setting to mexico

#A clock that refreshes every second
while True:
    dt = datetime.datetime.now()
    print(dt.strftime("%I:%M:%S %p")) 
    time.sleep(1)
    system('clear')