def isAngstrom(n):
  sum = 0
  order = len(n)

  for i in n:
    sum = sum + int(i)**order

  return sum == int(n)   

print("Please enter a number: ")
num = input()
if flag := isAngstrom(num):
  print(num, "is an Angstrom number")
else:
  print(num, "is NOT an Angstrom number")
