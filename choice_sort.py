massive = [1,12,2,3,2,12,24,54,6,54,321,123]
def choice_sort(A):
	N = len(A)
	for pos in range(1, N):
		for k in range(N):
			if A[pos]<A[k]:
				A[k], A[pos] = A[pos], A[k]
choice_sort(massive)
print(massive)
