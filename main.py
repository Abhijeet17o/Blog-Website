from flask import Flask, render_template
import requests

app = Flask(__name__)

ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"
RESPONSE = requests.get(ENDPOINT).json()

@app.route('/')
def home():    
    return render_template("index.html", blog_data=RESPONSE)

@app.route('/read/<index>')
def read_page(index):
    return render_template("post.html", blog_data1=RESPONSE, index_num=(int(index)-1))

if __name__ == "__main__":
    app.run(debug=True)
