import requests
import datetime
import time
import os 

last_exe = None


    
def message():
    os.system("cls")
    url = "http://checkip.amazonaws.com"
    request = requests.get(url)
    ip = request.text
    print(ip)

    dc_channel = ""
   



    payload = {
        "content":ip
    }

    headers = {""
            
            }
    res = requests.post(dc_channel,payload,headers=headers)



    time = datetime.datetime.now()
    
   
def cooldown():
    print("Currently sleeping")
    time.sleep(10)

while True: 
    time_now = datetime.datetime.now()
    day = time_now.day
    
    hour = time_now.hour
    if hour >= 3 and day != last_exe:
            last_exe = day
            message()
    else: 
        cooldown()