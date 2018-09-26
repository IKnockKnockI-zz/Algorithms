massive = list(range(10)) + list(range(5))
def insert_sort(A):
	N = len(A)
	for top in range(N):
		k = top
		while k > 0 and A[k-1]>A[k]:
			A[k], A[k-1] = A[k-1], A[k]
			k -= 1
insert_sort(massive)
print(massive)
