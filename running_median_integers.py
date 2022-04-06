# Problem: Find Median from Data Stream

def findMedian(stream):
  # print(stream)
  streamSize = len(stream)

  if streamSize == 1:
    return stream[0]
  stream = sorted(stream)
  midPt = streamSize // 2

  return (stream[midPt] if streamSize % 2 == 1 else
          (stream[midPt] + stream[midPt - 1]) // 2)

def findRunningMedian(inputArray):
  medianArray = []

  for i in range(len(inputArray)):
    # print(inputArray)
    currentMedian = findMedian(inputArray[:i+1])
    medianArray.append(currentMedian)

  return medianArray


solution = findRunningMedian([1, 2, 3, 4, 5])
print(solution)  
