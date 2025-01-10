from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Benvenuto su Giancarlo</h1><p>La tua landing page è attiva!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
