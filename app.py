from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("hello world!")
    return "svc app works!"

if __name__ == "__main__":
    app.run(host = '0.0.0.0')