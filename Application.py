from flask import  Flask, redirect, url_for, render_template, request
from operator import xor
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
In = ['A0','B0','C0','A1','B1','C1','A2','B2','C2','A3','B3','C3']
nIn = [None] * len(In)
@app.route("/Userinput", methods=["POST","GET"])
def login():
    if request.method == "POST":
    	for i in range(len(In)):
    		nIn[i]=(request.form[In[i]])
    	boy = func(nIn)
    	return render_template('Userinput.html', value1=boy,value2=69)
    else:
    	return render_template("Userinput.html")

def func(inn):
	inn = list(map(int,inn))  
	lst = [0,0,0,0,0,1,0,1,0,0,1,1]
	return (list(map(xor,inn,lst)))



