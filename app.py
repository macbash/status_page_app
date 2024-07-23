from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

services = {
    "Google": "https://www.google.com",
    "GitHub": "https://www.github.com",
    "Twitter": "https://www.twitter.com"
}

def check_service_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Operational"
        else:
            return "Down"
    except requests.exceptions.RequestException:
        return "Down"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status')
def status():
    service_statuses = {name: check_service_status(url) for name, url in services.items()}
    return jsonify(service_statuses)

if __name__ == '__main__':
    app.run(debug=True)
