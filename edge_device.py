import requests
import time
from cryptography.fernet import Fernet

def boot():
    print("\n--- [BOOT] Edge Device System ---")
    print("FileSystem: [ LOCKED ] (Encrypted Partition)")
    
    # ВАЖНО: используем host.docker.internal для связи с Windows
    url = "http://host.docker.internal:5000/get_key"
    
    try:
        print(f"Federation: Requesting key from {url}...")
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            # Получаем ключ из JSON ответа сервера
            key_received = response.json()['key'].encode()
            cipher = Fernet(key_received)
            
            # Читаем зашифрованный файл secret.data
            with open("secret.data", "rb") as f:
                encrypted_content = f.read()
            
            # Расшифровываем данные
            decrypted = cipher.decrypt(encrypted_content)
            
            print(f"Federation: [ SUCCESS ] Key received from Gateway")
            print(f"Action: Mounting Partition...")
            print(f"CONTENT: {decrypted.decode()}\n")
        else:
            print(f"Federation: [ FAILED ] Server returned status {response.status_code}")

    except Exception as e:
        print(f"Federation: [ FAILED ] Connection error: {e}")
        print("Action: Data stays encrypted.\n")

if __name__ == "__main__":
    boot()
    # Оставляем контейнер активным для демонстрации
    while True: 
        time.sleep(10)