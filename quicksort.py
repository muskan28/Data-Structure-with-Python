def quick_sort(A,low,high):
	if low<high:
		pivot = partition(A,low,high)
		quick_sort(A,low,pivot-1)
		quick_sort(A,pivot+1,high)

def partition(A,low, high):
	pivot= low
	swap(A,pivot,high)
	for i in range(low,high):
		if A[i]<=A[high]:
			swap(A,i,low)
			low +=1
	swap(A,low,high)
	return low
def swap(A,x,y):
	temp= A[x]
	A[x]= A[y]
	A[y]= temp

A=[112,432,42,4212,4344,45678,854,31,90]
print("before sorting",A)
quick_sort(A,0,len(A)-1)
print("after sorting",A)