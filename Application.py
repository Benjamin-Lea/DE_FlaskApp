from flask import  Flask, redirect, url_for, render_template, request
import py_functions as fc
app = Flask(__name__)
##variables##    
input_variables = [ 'A0','B0','C0','D0',
                    'A1','B1','C1','D1',
                    'A2','B2','C2','D2',
                    'A3','B3','C3','D3',
                    'A4','B4','C4','D4',
                    'A5','B5','C5','D5',
                    'A6','B6','C6','D6',
                    'A7','B7','C7','D7',
                    'A8','B8','C8','D8',
                    'A9','B9','C9','D9',
                    'A10','B10','C10','D10',
                    'A11','B11','C11','D11',
                    'A12','B12','C12','D12',
                    'A13','B13','C13','D13',
                    'A14','B14','C14','D14',
                    'A15','B15','C15','D15']

user_input = [None] *len(input_variables)
#user_input = []
binary = [0,0,0,0,
          0,0,0,1,
          0,0,1,0,
          0,0,1,1,
          0,1,0,0,
          0,1,0,1,
          0,1,1,0,
          0,1,1,1,
          1,0,0,0,
          1,0,0,1,
          1,0,1,0,
          1,0,1,1,
          1,1,0,0,
          1,1,0,1,
          1,1,1,0,
          1,1,1,1] 
num = 3
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/Userinput", methods=["POST","GET"])
def Userinput():
    if request.method == "POST":
    	for i in range(2**num):
            for j in range(num):
                user_input[4*i+j]=(request.form[input_variables[4*i+j]])
                #user_input.append(request.form[input_variables[4*i+j]])
    	T_data = fc.T_compair(user_input,binary,num)
    	T_data = ''.join(str(i) for i in T_data)
    	next_state = ''.join(str(i) for i in user_input)
    	return redirect(url_for("T_Output",T_data = T_data,next_state=next_state))
    else:
    	return render_template("Userinput.html",input_variables=input_variables,bin=binary)

@app.route("/T_Output/<T_data>/<next_state>")
def T_Output(T_data,next_state): 
    #eqA= fc.Eq(T_data,0,binary,num)#Pass 0 for A , 1 for B and 2 for C
    #eqB= fc.Eq(T_data,1,binary,num)
    #eqC= fc.Eq(T_data,2,binary,num)
    #eqD= fc.Eq(T_data,3,binary,num)
    return render_template('OutPutBase.html', T_data = T_data,
     next_state=next_state,bin=binary,eqA=1,eqB=2,eqC=3)

@app.route("/JK_Userinput", methods=["POST","GET"])
def JK_Userinput():
    if request.method == "POST":
        for i in range(len(input_variables)):
            user_input[i]=(request.form[input_variables[i]])
        JK_data = fc.JK_compair(user_input) #
        JK_data = ''.join(str(i) for i in JK_data)
        next_state = ''.join(str(i) for i in user_input)
        return redirect(url_for("JK_Output", JK_data = JK_data, next_state=next_state))
    else:
        return render_template("Userinput.html", input_variables=input_variables , bin = binary)

@app.route("/JK_Output/<JK_data>/<next_state>")
def JK_Output(JK_data,next_state):
    return render_template('JK_Output.html',JK_data = JK_data,
     next_state=next_state,bin=binary)