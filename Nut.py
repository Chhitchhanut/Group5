numbers = [42, 7, 89, 13, 56, 24, 68, 3, 91, 35, 76, 18, 60, 27, 84, 9, 31, 99, 50, 11, 66, 5, 74, 39, 20]

# Exercise 1: Calculate the Average
# Task: Find and print the average value of all the numbers in the array.
def sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

def average(total,arr):
    average = total / len(arr)
    return average

print(average(sum(numbers), numbers))
print()

