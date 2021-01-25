from win10toast import ToastNotifier
import psutil
import requests
import time

battery = psutil.sensors_battery()
percent = battery.percent
plugStat = battery.power_plugged

isLow = False
toaster = ToastNotifier()
url = 'https://maker.ifttt.com/trigger/battery_low/with/key/jSSEFX0LJxQmKnLTPKz80yifrypefKi0IaiuOkJn8eP'

while(True):
    if(percent <= 20 and plugStat == False and isLow == False):
        toaster.show_toast("Battery Low", "Turning on the smart plug.")
        deviceStat = requests.post(url) # Will turn on the socket
        isLow = True

    elif(percent <= 20 and plugStat == True and isLow == True):
        isLow = False
    
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugStat = battery.power_plugged

    time.sleep(15)