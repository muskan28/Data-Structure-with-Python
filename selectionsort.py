def selection_sort(S):
	for i in range(len(S)):
		least = i
		for k in range(i+1,len(S)):
			if S[k]<S[least]:
				least=k
		swap(S,least,i)
def swap(S,x,y):
	temp=S[x]
	S[x]= S[y]
	S[y]= temp

S=[21,33,42,1,34,99,77,86,54,311,765]
print('befor swap',S)
selection_sort(S)
print('after swap',S)