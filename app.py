from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'API Online!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run()
