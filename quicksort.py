def partial(A,start,end):
  pivot = A[end]
  pIndex = start

  for i in range(start,end):
    if A[i] <= pivot:
      A[i],A[pIndex] = A[pIndex],A[i]
      pIndex += 1

  A[pIndex],A[end] = A[end],A[pIndex]

  return pIndex



def quicksort(A,start,end):

  if start < end:
    pIndex = partial(A,start,end)
    quicksort(A,start,pIndex-1)
    quicksort(A,start+1,pIndex)




A = [7,9,0,2,3,4]
quicksort(A,0,5)
print("The sorted array using quick sort algorithm:")
for i in range(0,5):
    print(A[i])
