from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
print(response[0]["body"])

print("\n\n")

for post in response :
    print(post["title"])
    
@app.route("/")
def start():
    return render_template("index.html")

if __name__ == "__main__" :
    app.run(port=8080)
    
