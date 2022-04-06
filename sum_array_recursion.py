# Write a program to sum a given array
# using recursion

def recur_sum(arr, i):
  #print(arr[i])
  return arr[i] if i < 1 else arr[i] + recur_sum(arr, i-1)


arr = [-1, 2, -3, 4, 5]
print(recur_sum(arr, len(arr)-1))
