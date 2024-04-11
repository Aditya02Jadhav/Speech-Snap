from flask import Flask, render_template, request
import os

# import cap_load.py
from cap_load import caption_this_image


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def marks():
    if request.method == 'POST':
        f = request.files['userfile']
        path = "./static/{}".format(f.filename)
        f.save(path) 
        result_dic = caption_this_image(path)
        


    return render_template("index.html", your_result =result_dic)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/faqs')
def faqs():
    return render_template("faqs.html")

@app.route('/team')
def team():
    return render_template("team.html")

    
if __name__ == "__main__":
    app.run(debug=True)
