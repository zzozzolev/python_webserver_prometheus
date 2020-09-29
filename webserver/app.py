from flask import Flask
import prometheus_client

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello :)"

@application.route("/metrics")
def metrics():
    return ""

if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0')