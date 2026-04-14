from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "URL Status API Running"})

@app.route("/check/<path:url>")
def check(url):
    try:
        response = requests.get(f"http://{url}", timeout=5)
        return jsonify({
            "url": url,
            "status_code": response.status_code,
            "status": "UP"
        })
    except:
        return jsonify({
            "url": url,
            "status": "DOWN"
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)