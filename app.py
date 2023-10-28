from flask import Flask, render_template, request, jsonify
import subprocess
import os
from caesar import caesar as c1 # first cipher
from substitution import substitution as c2 # second cipher
from generate import generate as gn

app = Flask(__name__)

@app.route("/")
def index():
    # Construct the absolute path to the Markdown file
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def submit():
    text = request.json.get("text")
    print(text)
    gen=gn()
    value=gen.getrandom(1)[0]
    cipher1=c1(int(value),text)
    encrypted = cipher1.encrypt()
    print(encrypted)
    
    return jsonify("Encrypted Values: "+str(encrypted))

@app.route("/submit2", methods=["POST"])
def submit2():
    import os
    import sys

    curr_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.join(curr_dir,'..','passion-backend'))

    import aiprediction
    print("chekcpoint")
    
    text = request.json.get("text")
    print(text)
    prediction = aiprediction.aiprediction()
    output=prediction.pred(text)
    
    return jsonify("Encrypted Values: "+str(output))

if __name__ == "__main__":
     app.run(debug=True)