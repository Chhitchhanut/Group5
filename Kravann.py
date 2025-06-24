array2D = [ [12, 3, 19, 0, 7],
            [8, 14, 6, 2, 17],
            [11, 20, 1, 13, 9],
            [4, 10, 5, 18, 16],
            [0, 15, 3, 19, 6]
            ]
newArray = []
for row in (array2D):
    sum = 0 
    for col in row:
      sum+= col
    newArray.append(sum)
print(newArray)