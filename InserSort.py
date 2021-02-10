def InsertSort(arr):
    for i in range(1,len(arr)):

        value =arr[i]
        position = i

        while position > 0 and arr[position-1] > value:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = value



arr = [5,2,4,6,7]
InsertSort(arr)
for i in range(len(arr)):
    print(arr[i])
