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

