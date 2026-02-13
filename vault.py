from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())

# Статичный ключ для нашей симуляции
key = b'u7_G9_X9_K-T-8W7j-5L-W3-L_L1_K-T-8W7j-5L-W3-L='
cipher = Fernet(key)

# Текст, который мы прячем
secret_info = "ACCESS_GRANTED: SmartCity_CCTV_Feed_01_Active"

with open("secret.data", "wb") as f:
    f.write(cipher.encrypt(secret_info.encode()))

print("Файл secret.data создан. Теперь он зашифрован!")