#Function for Binary Search
def binary_search(A, x, y, f):
	if y >= x:
		m = int((y + x)//2)
		if A[m] == f:
			return m
		elif A[m] > f:
			return binary_search(A, x, m - 1, f)
		else:
			return binary_search(A, m + 1, y, f)
	else:
		return -1

#Testing Binary Search Function
A = [2,3,4,10,40,60]
f = 15

final = binary_search(A, 0, len(A)-1, f)

#Printing out Result
if final != -1:
	print("Element is present at index", str(final))
else:
	print("Element is not present in array")
