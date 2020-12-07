def day3():
  f = open("./day3input.txt", "r")

  lines = []

  for x in f:
    lines.append(x)
  
  trees = 0
  slope = 3
  position = 0
  i = 0
  length = len(lines[0]) - 1


  for x in lines:

    if position >= length:
      position = position - length

    if lines[i][position] == "#":
      trees += 1
    
    position += slope
    i += 1

  print(trees)

  f.close()

day3()