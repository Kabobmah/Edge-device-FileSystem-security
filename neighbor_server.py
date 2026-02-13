from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_key')
def give_key():
    # Тот самый ключ, который "отпирает" систему
    return jsonify({"status": "authorized", "key": "ENTERPRISE_SECRET_2026"})

if __name__ == "__main__":
    # Запускаем на порту 5000
    app.run(host='0.0.0.0', port=5000)