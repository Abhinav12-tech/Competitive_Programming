def countingSort(arr):
    count = [0]*(max(arr)+1)
    res = [0]*len(arr)
    for num in  arr:
        count[num] = count[num]+1
    for i in range(1,len(count)):
        count[i] = count[i-1]+count[i]
    for num in arr:
        res[count[num]-1] = num
        count[num] = count[num]-1
    print("The sorted array is ", res)
    return


if __name__ == "__main__":
  arr = [5,2,4,2,1,5,1,5]
  print("The original array is ",arr)
  countingSort(arr)
