from flask import Flask, render_template, request, jsonify
import subprocess
import os
import caesar as c1 # first cipher
import substitution as c2 # second cipher
import generate
app = Flask(__name__)

@app.route("/")
def index():
    # Construct the absolute path to the Markdown file
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def submit():
    text = request.json.get("text")
    gen=generate()
    value=gen.getrandom(1)
    mycipher = c1(3,text)
    print(mycipher)
    response = {"message": f"You submitted the text: {text}"}
    return jsonify(response)

if __name__ == "__main__":
     app.run(debug=True)