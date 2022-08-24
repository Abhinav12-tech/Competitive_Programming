def linsearch(List, n):

	for i in range(len(List)):
		if List[i] == n:
			return i
	return -1

a = [1,2,3,4,5,6]
n = 4

final = linsearch(a, n)
if final!=-1:
    print("Element found in list at index", str(final))
else:
    print("Element not found")
