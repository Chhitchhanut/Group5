array = [1,2,3,4,0,5,11,6,7,8,9,10]
sum = 0
for char in array:
    sum += char
print(sum)
#

array = [1,2,3,4,0,5,11,6,7,8,9,10]
sum_odd = 0
for char in array:
    if char % 2 == 1:
        sum_odd += char
print(sum_odd)
