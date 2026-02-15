from cryptography.fernet import Fernet
import os

key = b'pZQ9900UZ1nW3_Lc-V4aG7htp0bxf8x8niD_9ljRT6g=' 
cipher = Fernet(key)
print(cipher)

def encrypt():
    if not os.path.exists("message.txt"):
        with open("message.txt", "w") as f:
            f.write("DEFAULT_SECRET_DATA_001")
    
    with open("message.txt", "r") as f:
        text = f.read()

    with open("secret.data", "wb") as f:
        f.write(cipher.encrypt(text.encode()))

    print(f"Done! 'secret.data' created with message: {text}")

if __name__ == "__main__":
    encrypt()