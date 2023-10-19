from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")

all_posts = response.json()
print("\n\n")

'''for post in response :
    print
    (post["title"])'''
    
@app.route("/")
def start():
    return render_template("index.html", posts=all_posts)

@app.route("/read/<int:id>")
def read(id):
    for post in all_posts : 
        if post["id"] == id :
            blog = post
            break
        
    
    return render_template("post.html",posts = blog)


if __name__ == "__main__" :
    app.run(port=8080)
    
