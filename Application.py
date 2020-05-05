from flask import  Flask, redirect, url_for, render_template, request
import py_functions as fc
app = Flask(__name__)
##variables##    
input_variables = ['A0','B0','C0',
                   'A1','B1','C1',
                   'A2','B2','C2',
                   'A3','B3','C3',
                   'A4','B4','C4',
                   'A5','B5','C5',
                   'A6','B6','C6',
                   'A7','B7','C7']

user_input = [None] *len(input_variables)
binary = [0,0,0,
          0,0,1,
          0,1,0,
          0,1,1,
          1,0,0,
          1,0,1,
          1,1,0,
          1,1,1] 


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Userinput", methods=["POST","GET"])
def login():
    if request.method == "POST":
    	for i in range(len(input_variables)):
    		user_input[i]=(request.form[input_variables[i]])
    	T_data = fc.T_compair(user_input)
    	T_data = ''.join(str(i) for i in T_data)
    	next_state = ''.join(str(i) for i in user_input)
    	return redirect(url_for("Output", T_data = T_data, next_state=next_state))
    else:
    	return render_template("Userinput.html", input_variables=input_variables , bin = binary)

@app.route("/Output/<T_data>/<next_state>")
def Output(T_data,next_state): 
    eqA= fc.Eq(T_data,0)#Pass 0 for A , 1 for B and 2 for C
    return render_template('OutPutBase.html', T_data = T_data, next_state=next_state,bin = binary,eqA=eqA)



