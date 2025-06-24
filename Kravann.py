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

numbers = [42, 7, 89, 13, 56, 24, 68, 3, 91, 35, 76, 18, 60, 27, 84, 9, 31, 99, 50, 11, 66, 5, 74, 39, 20]
def isEven(num):
    if num % 2 == 0:
      return True
    return False

countEven = 0
countOdd = 0
for num in numbers:
    if (isEven(num)):
      countEven += 1
    else:
      countOdd += 1
print(countOdd)
print(countEven)



nums = [1,2,77,10,8]
for i in nums:
    if i > 9 and i < 100:
        print(i)