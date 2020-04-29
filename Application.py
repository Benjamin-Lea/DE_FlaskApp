from flask import  Flask, redirect, url_for, render_template, request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
value = [2,2]
@app.route("/Userinput", methods=["POST","GET"])
def login():
    if request.method == "POST":
    	value[0] = request.form['C1']
    	value[1] = request.form['C2']
    	return render_template('Userinput.html', value1=value[0],value2=value[1])
    else:
    	return render_template("Userinput.html")



