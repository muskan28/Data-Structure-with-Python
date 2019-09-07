def insertion_sort(S):
	for i in range(1,len(S)):
		temp=S[i]
		k=i
		while k>0 and temp<S[k-1]:
			S[k] = S[k-1]
			k -=1
		S[k]=temp
S=[32,33,1,23,65,77]
print('before sort',S)
insertion_sort(S)
print('after sort',S)
