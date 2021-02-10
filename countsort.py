def countsort(array, maxvalue):
  m = maxvalue + 1
  count = [0] * m 
  
  for i in array:  # count how many times a number appear
    count[i] += 1
    
  i = 0
  for a in range(m):
    for b in range(count[a]):
      array[i] = a
      i += 1
      
  retrun array
  
 print(countsort([8,4,5,6,7,8,9,1,2,1,1,3],9))
  
  """ Time complexity for this algirithm O(n+k) where n is the number of elements in input array and k is the range of input"""
  
  
  
  
  
 
