#min jumps array.py
def jump(self,A):
	i = len(A)
	count = 0
	pos = 0
	for i in range(1,1):
		A[i]= max(1+A[1], A[i-1])
	while(pos <i-1):
		if(pos>= A[pos]):
			return-1
		if(pos< A[pos]):
			count+=1
			pos=A[pos]
		return count