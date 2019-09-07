def merge_sort(A):
	if(len(A)>1):
		mid=len(A)//2
		lefthalf=A[:mid]
		righthalf= A[mid:]
		merge_sort(lefthalf)
		merge_sort(righthalf)
		i=j=k=0
		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i]<righthalf[j]:
				A[k]=lefthalf[i]
				i= i+1

			else:
				A[k]=righthalf[j]
				j=j+1

			k=k+1

			while i<len(lefthalf):
				A[k]= lefthalf[i]
				i=i+1
				k=k+1
				
			while j<len(righthalf):
				A[k]=righthalf[j]
				j=j+1
				k=k+1
				
A=[221,342,56,211,5543,54,21,55,212,88]
print('before sort',A)
merge_sort(A)
print('after sort',A)