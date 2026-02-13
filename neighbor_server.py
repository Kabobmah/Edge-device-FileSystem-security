from flask import Flask, jsonify

app = Flask(__name__)

# Тот же самый ключ, что в vault.py
FERNET_KEY = "pZQ99OOUZ1nW3_Lc-V4aG7htP0bxF8x8niD_9ljRT6g="

@app.route('/get_key')
def give_key():
    return jsonify({
        "status": "authorized",
        "gateway": "Building_Gateway_01",
        "key": FERNET_KEY
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)