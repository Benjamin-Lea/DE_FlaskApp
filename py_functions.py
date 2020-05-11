from operator import xor
def T_compair(T_data,binary,num): 
	T_data = list(map(int,T_data))
	for i in range(2**num):
		for j in range(num):
			T_data[i*num+j] = xor(T_data[i*num+j],binary[i*4+j+(4-num)])
	T_data = ''.join(str(i) for i in T_data)
	return T_data 

def Eq(Data,ABC,binary,num):#Pass 0 for A , 1 for B and 2 for C
  Data = list(map(int, str(Data))) 
  eq =[]
  for o in range((2**num)):
  	if Data[o*num+ABC]==1:
  		for j in range(num):
  			if j==0:
  				if(len(eq)>0):
  					eq.append(" + ")
  				if binary[o*4+j+(4-num)]==1:
  					eq.append("(A")
  				else:
  					eq.append("(~A")
  			elif j==1:
  				if binary[o*4+j+(4-num)]==1:
  					eq.append("B")
  				else:
  					eq.append("~B")
  			elif j==2:
  				if binary[o*4+j+(4-num)]==1:
  					eq.append("C")
  				else:
  					eq.append("~C")
  			elif j==3:
  				if binary[o*4+j+(4-num)]==1:
  					eq.append("D")
  				else:
  					eq.append("~D")
  		eq.append(")")
  eq= ''.join(str(i) for i in eq)
  if eq == '':
    return "0"
  return eq

def JK_compair(jk_data,num):
	if(num ==2):
		binary = [0,0,0,1,1,0,1,1]
	if(num==3):
		binary = [0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,1,1,1]
	if(num ==4):
		binary = [0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1,
          					1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1] 
	jk = []
	print(jk_data)
	for o in range(len(binary)):
		if(binary[o]==1):
			jk.append("X")
		else:
			jk.append(str(jk_data[o]))
	for o in range(len(binary)):
		if(binary[o]==0):
			jk.append("X")
		else:
			jk.append(str(xor(int(jk_data[o]),1)))
	jk= ''.join(str(i) for i in jk)
	print(jk)
	return jk