from flask import Flask, jsonify

app = Flask(__name__)

# Тот же ключ, что используется для шифрования в vault.py
FERNET_KEY = "pZQ9900UZ1nW3_Lc-V4aG7htp0bxf8x8niD_9ljRT6g="

@app.route('/get_key')
def give_key():
    print("--- [GATEWAY] Request received! Sending key... ---")
    return jsonify({
        "status": "authorized",
        "gateway": "Building_Gateway_01",
        "key": FERNET_KEY
    })

if __name__ == "__main__":
    # Слушаем на всех интерфейсах (0.0.0.0)
    app.run(host='0.0.0.0', port=5000)