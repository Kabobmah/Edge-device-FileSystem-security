import requests
import time
from cryptography.fernet import Fernet

def boot():
    print("\n--- [BOOT] Edge Device System ---")
    print("FileSystem: [ LOCKED ] (Encrypted Partition)")
    
    try:
        # reaching neighbour
        r = requests.get("http://host.docker.internal:5000/get_key", timeout=5)
        if r.status_code == 200:
            key = r.json()['key'].encode()
            cipher = Fernet(key)
            
            # read and decrypt
            with open("secret.data", "rb") as f:
                decrypted = cipher.decrypt(f.read())
            
            print(f"Federation: [ SUCCESS ] Connected to {r.json()['gateway']}")
            print(f"Action: Mounting Partition...")
            print(f"CONTENT: {decrypted.decode()}\n")
    except:
        print("Federation: [ FAILED ] Gateway not found. Data stays encrypted.\n")

if __name__ == "__main__":
    boot()
    while True: time.sleep(10)