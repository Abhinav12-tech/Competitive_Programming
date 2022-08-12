#Function to create sub-arrays
def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m
	L = [0] * (n1)
	R = [0] * (n2)
	
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	i = 0
	j = 0
	k = l

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

#Function to sort and merge arrays into final array
def mergeSort(arr, l, r):
	if l < r:
		m = l+(r-l)//2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

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

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Input array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

f = 11

final = binary_search(arr, 0, len(arr)-1, f)

#Printing out Result
if final != -1:
	print("\n\nElement is present at index", str(final))
else:
	print("\n\nElement is not present in array")
