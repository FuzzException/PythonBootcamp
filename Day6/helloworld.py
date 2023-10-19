from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"
@app.route("/Bye")
def bye():
    return "<p>Bye Bye</p>"

if __name__=="__main__":
    app.run(port=8080)