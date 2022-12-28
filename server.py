from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    result = "Hello world".encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
