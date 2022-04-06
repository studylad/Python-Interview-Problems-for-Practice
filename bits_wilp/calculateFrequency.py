def calculateFrequency(str):
  nums = str.split()
  freq = {}

  for i in nums:
    if i in freq:
      freq[i] += 1

    else:
      freq[i] = 1
  print(freq)


print("Please enter the numbers seperated by space. \n Press ENTER to exit: ")
x = input()
calculateFrequency(x)
