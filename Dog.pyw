import requests
import time
import threading
import os

def send_startup_message():
     
    
    bot_id = "-"
    chat_id = "-"
    params = {
        "chat_id": chat_id,
        "text": "Computer turn on"
    }
    i = 1
    while i != 0:
        try:
             
            response = requests.get(f"https://api.telegram.org/bot{bot_id}/sendMessage", params=params)
            i = 0  
        except:
            i = 1
            
            time.sleep(5)   

def monitor_messages():
     
    bot_id = "-"
    last_update_id = None
    url = f"https://api.telegram.org/bot{bot_id}"

    while True:
        try:
            
            response = requests.get(f"{url}/getUpdates", params={"offset": last_update_id})
            data = response.json()
            
             
            if data["result"]:
                 
                latest_update = data["result"][-1]
                last_update_id = latest_update["update_id"] + 1

                if "message" in latest_update:
                    chat_id = latest_update["message"]["chat"]["id"]
                    message_text = latest_update["message"]["text"].lower()
                    
                     
                    if "pc-sht" in message_text:
                        
                        os.system('shutdown /s /f /t 0')
                        return   

            time.sleep(2)   
        except Exception as e:
            print(f"error  {e}")
            time.sleep(5)  

 
startup_thread = threading.Thread(target=send_startup_message)
monitor_thread = threading.Thread(target=monitor_messages)

startup_thread.start()
monitor_thread.start()

 
startup_thread.join()
monitor_thread.join()
