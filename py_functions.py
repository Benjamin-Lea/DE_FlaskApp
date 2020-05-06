from operator import xor
def T_compair(T_data,binary,num): 
	T_data = list(map(int,T_data))
	for i in range(2**num):
		for j in range(num):
			T_data[i*num+j] = xor(T_data[i*num+j],binary[i*4+j+(4-num)])
	T_data = ''.join(str(i) for i in T_data)
	print(T_data)
	return T_data 

def Eq(Data,ABC,binary,num):#Pass 0 for A , 1 for B and 2 for C
  Data = list(map(int, str(Data))) 
  eq =[]
  if(ABC == 0):
    a=0
  if(ABC == 1):
    a=-1
  if(ABC == 2):
    a=-2
  if(ABC == 3):
    a=-3
  for o in range(len(binary)):
    if o%4==ABC:
      c=a
      if Data[o]==1:
        for i in range(num):
          if i==0:
            if(len(eq)>0):
              eq.append(" + ")
            if binary[o+c]==1:
              eq.append("(A")
            else:
              eq.append("(~A")
            c=c+1
          elif i==1:
            if binary[o+c]==1:
              eq.append("B")
            else:
              eq.append("~B")
            c=c+1
          elif i==2:
            if binary[o+c]==1:
              eq.append("C)")
            else:
              eq.append("~C")
            c=c+1
          elif i==3:
            if binary[o+c]==1:
              eq.append("D")
            else:
              eq.append("~D")
          eq.append(")")
  eq= ''.join(str(i) for i in eq)
  if eq == '':
    return "0"
  return eq

def JK_compair(jk_data):
	binary = [0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,1,1,1] 
	jk = []
	for o in range(len(binary)):
		if(binary[o]==1):
			jk.append("X")
		else:
			jk.append(str(jk_data[o]))
	for o in range(len(binary)):
		if(binary[o]==0):
			jk.append("X")
		else:
			jk.append(str(jk_data[o]))
	jk= ''.join(str(i) for i in jk)
	return jk