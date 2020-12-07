def day3p2():
  f = open("./day3input.txt", "r")

  lines = []

  for x in f:
    lines.append(x)
  
  results = []
  result = 0
  trees = 0
  position = 0
  i = 0
  j = 0
  length = len(lines[0]) - 1

  right = [1, 3, 5, 7, 1]
  down = [1, 1, 1, 1, 2]

  for x in right:

    for x in lines:

      if position >= length:
        position = position - length
      
      if i < len(lines):
        if lines[i][position] == "#":
          trees += 1

      position += right[j]
      i += down [j]
    
    results.append(trees)
    trees = 0
    position = 0
    i = 0
    j += 1

  result = results[0] * results[1] * results[2] * results[3] * results[4]

  print(result)

  f.close()

day3p2()

# make an array with slopes to test
# test all and multiply values