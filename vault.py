from cryptography.fernet import Fernet

# Генерируем ключ (запомни его, он должен быть одинаковым везде)
# Для удобства используем фиксированный валидный ключ:
key = b'pZQ99OOUZ1nW3_Lc-V4aG7htP0bxF8x8niD_9ljRT6g=' 
cipher = Fernet(key)

secret_data = "SEC-PRJ-6_23: TOP_SECRET_CITY_DATA_AUTHORIZED"

with open("secret.data", "wb") as f:
    f.write(cipher.encrypt(secret_data.encode()))

print(" 'secret.data' encrypted")