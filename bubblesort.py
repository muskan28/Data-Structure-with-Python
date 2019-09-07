def bubble_sort(S):
 for i in range(len(S)):
 	for k in range(len(S)-1,i,-1):
 		if(S[k]<S[k-1]):
 			Swap(S,k,k-1)

def Swap(S,p,q):
	temp= S[p]
	S[p]= S[q]
	S[q]= temp

S=[21,34,56,22,11,67,21,38,90]
print('Before swapping',S)
bubble_sort(S)
print('After Swapping',S)

