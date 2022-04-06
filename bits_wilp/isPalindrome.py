def isPalindrome(str):
  return str == str[::-1]   

print("Please enter a string: ")
x = input()
if flag := isPalindrome(x):
  print(x, "is a Palindrome")
else:
  print(x, "is NOT a Palindrome")
