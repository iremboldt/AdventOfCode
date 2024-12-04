def advent1(input):
  file = open(input,'r')
  lines_list = file.readlines()
  cols, rows = (int(val) for val in lines_list[0].split())
  data = [[int(val) for val in line.split()] for line in lines_list[0:]]
  #https://stackoverflow.com/questions/6583573/how-to-read-numbers-from-file-in-python
  
  left, right = zip(*data)
  #https://stackoverflow.com/questions/7558908/unpacking-a-list-tuple-of-pairs-into-two-lists-tuples
  
  left=sorted(left)
  right=sorted(right)
  
  distance=[]
  for i in range(len(left)):
      dist=[abs(left[i]-right[i])]
      distance += dist
  #https://stackoverflow.com/questions/55368218/how-can-i-subtract-the-values-in-two-lists-with-the-same-lengths-in-python-witho
  
  final=sum(distance)
  return(final)
