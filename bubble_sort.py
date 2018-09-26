massive = [1,2,4,5,6,32,45,654,32,132,53,67,56575]
def bubble_sort(A):
	N = len(A)
	for x in range(1, N):
		for k in range(0, N-x):
			if A[k]>A[k+1]:
				A[k], A[k+1] = A[k+1], A[k]
bubble_sort(massive)
print(massive)
