student_ages = [15, 18, 20, 17, 16, 25]
youngest_age = student_ages[0]
for i in range(len(student_ages)):
    if youngest_age > student_ages[i]:
        youngest_age = student_ages[i]
print(youngest_age)

student_ages = [15, 18, 20, 17, 16, 25]
max = student_ages[0]
for i in range(len(student_ages)):
    if student_ages[i]> max:
        max = student_ages[i]
print(max)