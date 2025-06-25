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

# Exercise 2: Count Even and Odd Numbers
# Task: Count and print how many even numbers and how many odd numbers are in the array.
def find_odd(arr):
    odd_num = []
    for num in arr:
        if num % 2 == 1:
            odd_num.append(num)
    return odd_num

def find_even(arr):
    even_num = []
    for num in arr:
        if num % 2 == 0:
            even_num.append(num)
    return even_num

def count(arr):
    count_num = 0
    for num in arr:
        count_num += 1
    return count_num

print('Count of even numbers in the array is', count(find_even(numbers)))
print('Count of odd numbers in the array is', count(find_odd(numbers)))
print()

