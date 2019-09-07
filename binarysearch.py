def binary_search(A,low,high,value):
	A.sort()
	mid=(low+high)//2
	if low<=high:
		if(A[mid]==value):
			return mid
		elif(A[mid]>value):
			return binary_search(A,low,mid-1,value)
		elif(A[mid]<value):
			return binary_search(A,mid+1,high,value)
	return -1
A=[34,78,98,99,54,67,90]
print(binary_search(A,0,len(A)-1,90))