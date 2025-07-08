from flask import Flask

this = Flask(__name__)

@this.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    this.run(debug=True)
