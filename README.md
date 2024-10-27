```markdown
# 🐾 WatchDogBot 👁️

**Take control of your computer remotely, get notified every time it boots up, and shut it down with a single message whenever needed!** WatchDogBot allows you to manage your computer via Telegram. 📲💻

## 🚀 Features

- **🔔 Instant Notifications**: Get notified as soon as your computer is turned on.
- **🔒 Remote Shutdown**: Shut down your computer with a single command sent from Telegram.

Your computer now awaits your commands from afar! It’s that powerful and easy to use! 💪

---

## 📥 Installation Steps

### 1. Create Your Bot on Telegram

1. Start a conversation with [BotFather](https://t.me/BotFather) on Telegram.
2. Type **`/newbot`** and press Enter, then give your bot a name.
3. Save the API **bot token** provided. You’ll use this token to access your bot.

#### 📌 Where to Place the Token?

Enter the token you received into the `bot_id` variable in the code below:

```python
bot_id = "YOUR_BOT_TOKEN_HERE"
```

### 2. Get Your Chat ID

1. Send a **`/start`** message to your new bot on Telegram.
2. Run the following Python code to obtain your chat ID:

   ```python
   import requests
   
   bot_id = "YOUR_BOT_TOKEN_HERE"
   url = f"https://api.telegram.org/bot{bot_id}/getUpdates"
   
   response = requests.get(url)
   data = response.json()
   
   chat_id = data["result"][0]["message"]["chat"]["id"]
   print("Chat ID:", chat_id)
   ```

3. Note the **chat ID** that appears. This ID tells the bot who it will be communicating with.

#### 📌 Where to Place the Chat ID?

Add this number to the `chat_id` variable to specify where the bot will send messages:

```python
chat_id = "YOUR_CHAT_ID_HERE"
```

### 3. Set Up and Run WatchDogBot

The following code configures your bot to send you a message on Telegram whenever your computer starts up and listen for shutdown commands via Telegram.

```python
import requests
import time
import threading
import os

def send_startup_message():
    # Bot token and chat ID
    bot_id = "YOUR_BOT_TOKEN_HERE"
    chat_id = "YOUR_CHAT_ID_HERE"
    
    params = {
        "chat_id": chat_id,
        "text": "Computer has started up! 🎉"
    }
    
    while True:
        try:
            requests.get(f"https://api.telegram.org/bot{bot_id}/sendMessage", params=params)
            break
        except:
            print("Reconnecting...")
            time.sleep(5)

def monitor_messages():
    bot_id = "YOUR_BOT_TOKEN_HERE"
    chat_id = "YOUR_CHAT_ID_HERE"
    url = f"https://api.telegram.org/bot{bot_id}/getUpdates"
    last_update_id = None
    
    while True:
        try:
            response = requests.get(url, params={"offset": last_update_id})
            data = response.json()
            
            for update in data["result"]:
                last_update_id = update["update_id"] + 1
                message_text = update["message"]["text"].lower()

                if "pc-sht" in message_text:
                    print("Shutting down computer...")
                    os.system("shutdown /s /f /t 0")
                    return
            
            time.sleep(2)
        except Exception as e:
            print("An error occurred:", e)
            time.sleep(5)

threading.Thread(target=send_startup_message).start()
threading.Thread(target=monitor_messages).start()
```

### 4. Run at Startup

To make it launch automatically, create a `.bat` file:

1. Open Notepad and enter the following code (update the Python file path):

   ```bat
   @echo off
   python  dog.pyw
   ```

2. Save this file as `watchdogbot_start.bat`.
3. Press `Win + R`, type **`shell:startup`**, and press Enter to open the Startup folder. Move the `.bat` file to this folder.

---

**🎉 Congratulations!** WatchDogBot is now set to run on each startup and notify you on Telegram!
```


```markdown
# 🐾 WatchDogBot 👁️

**Bilgisayarınızı uzaktan kontrol edin, her açıldığında haberdar olun ve gerektiğinde tek bir mesajla kapatın!** WatchDogBot, Telegram üzerinden bilgisayarınızın kontrolünü size sunar. 📲💻

## 🚀 Özellikler

- **🔔 Anında Bildirim**: Bilgisayarınız açıldığında size anında mesaj gönderir.
- **🔒 Uzaktan Kapatma**: Telegram üzerinden tek bir komutla bilgisayarınızı kapatabilirsiniz.

Artık bilgisayarınız, sizin uzaktan verdiğiniz komutları bekliyor! İşte bu kadar güçlü ve kolay bir sistem! 💪

---

## 📥 Kurulum Adımları

### 1. Telegram’da Botunuzu Oluşturun

1. Telegram’da [BotFather](https://t.me/BotFather) ile sohbet başlatın.
2. **`/newbot`** yazıp Enter’a basın, botunuza bir ad verin.
3. Size verilen API **bot token’ını** kaydedin. Bu token ile botunuza erişim sağlayacağız.

#### 📌 Token’ı Nereye Yazacağım?

Aşağıdaki kodda `bot_id` değişkenine aldığınız token’ı yazın:

```python
bot_id = "BURAYA_BOT_TOKENINIZI_YAZIN"
```

### 2. Chat ID’nizi Alın

1. Yeni botunuza Telegram’dan **`/start`** mesajı gönderin.
2. Chat ID’nizi almak için aşağıdaki Python kodunu çalıştırın:

   ```python
   import requests
   
   bot_id = "BURAYA_BOT_TOKENINIZI_YAZIN"
   url = f"https://api.telegram.org/bot{bot_id}/getUpdates"
   
   response = requests.get(url)
   data = response.json()
   
   chat_id = data["result"][0]["message"]["chat"]["id"]
   print("Chat ID:", chat_id)
   ```

3. Çıkan **chat ID**’yi not edin. Bu ID, botunuzun kiminle konuşacağını belirler.

#### 📌 Chat ID’yi Nereye Yazacağım?

Botun mesaj göndereceği yeri belirlemek için `chat_id` değişkenine bu numarayı yazın:

```python
chat_id = "BURAYA_CHAT_ID_YAZIN"
```

### 3. WatchDogBot’u Kurun ve Çalıştırın!

Aşağıdaki kod, botunuzu bilgisayar açıldığında Telegram’da size bildirim gönderecek ve Telegram üzerinden gelen kapatma komutlarını takip edecektir.

```python
import requests
import time
import threading
import os

def send_startup_message():
    # Bot token ve chat ID
    bot_id = "BURAYA_BOT_TOKENINIZI_YAZIN"
    chat_id = "BURAYA_CHAT_ID_YAZIN"
    
    params = {
        "chat_id": chat_id,
        "text": "Bilgisayar açıldı! 🎉"
    }
    
    while True:
        try:
            requests.get(f"https://api.telegram.org/bot{bot_id}/sendMessage", params=params)
            break
        except:
            print("Tekrar bağlanıyor...")
            time.sleep(5)

def monitor_messages():
    bot_id = "BURAYA_BOT_TOKENINIZI_YAZIN"
    chat_id = "BURAYA_CHAT_ID_YAZIN"
    url = f"https://api.telegram.org/bot{bot_id}/getUpdates"
    last_update_id = None
    
    while True:
        try:
            response = requests.get(url, params={"offset": last_update_id})
            data = response.json()
            
            for update in data["result"]:
                last_update_id = update["update_id"] + 1
                message_text = update["message"]["text"].lower()

                if "pc-sht" in message_text:
                    print("Bilgisayar kapatılıyor...")
                    os.system("shutdown /s /f /t 0")
                    return
            
            time.sleep(2)
        except Exception as e:
            print("Hata oluştu:", e)
            time.sleep(5)

threading.Thread(target=send_startup_message).start()
threading.Thread(target=monitor_messages).start()
```

### 4. Başlangıçta Çalıştırın!

**Otomatik başlatma için** bir `.bat` dosyası oluşturun:

1. Not Defteri’ni açın ve şu kodu yazın (Python dosya yolunuzu güncelleyin):

   ```bat
   @echo off
   python yourdo.pyw"
   ```

2. Bu dosyayı `watchdogbot_start.bat` olarak kaydedin.
3. `Win + R` ile **`shell:startup`** yazın ve Başlangıç klasörüne girin. `.bat` dosyasını bu klasöre atın.

