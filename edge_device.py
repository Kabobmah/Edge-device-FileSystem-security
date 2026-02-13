import requests
import time

def boot_process():
    print("\n--- [BOOT] Edge Device System Starting... ---")
    print("FileSystem Status: [ LOCKED ] (Encrypted Partition)")
    
    try:
        # ВАЖНО: используем host.docker.internal для связи с Windows
        url = "http://host.docker.internal:5000/get_key"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            key = response.json().get('key')
            print(f"Federation: [ SUCCESS ] Key received: {key}")
            print("FileSystem Status: [ MOUNTED ] Access Granted.\n")
        else:
            print("Federation: [ DENIED ] Unauthorized Access.\n")
    except:
        print("Federation: [ ERROR ] Neighbor not found. Connection failed.")
        print("FileSystem Status: [ STAYING ENCRYPTED ]\n")

if __name__ == "__main__":
    boot_process()
    while True: time.sleep(10) # Чтобы контейнер не закрылся