#student1 Grades
# OOP = 94.67
# FL = 89.78
# BPO = 92.59
# CCT = 76.56
# PE3 = 89.57
# DSAL = 69.69
# STS = 85.00
# TCW = 76.00
# PT = 89.00

grades = [94.67, 89.78, 76.56, 89.57, 69.69, 85.00]
grades_rimando = [94.67, 89.78, 76.56, 89.57, 69.69, 85.00]
grades_franda = [94.67, 89.78, 76.56, 89.57, 69.69, 85.00]
sum = 0
for item in grades:
    sum = sum + item

average = sum/len(grades)

print(f"Average:{round(average,2)}")

# print(grades[0])
# print(grades[1])
# print(grades[2])
# print(grades[3])
# print(grades[4])
# print(grades[5])
# sum = OOP + FL + BPO + CCT + PE3 + DSAL + STS + TCW + PT
# average = sum/9
# average = round(average, 2)
# average = 97
    #false               and         true = false
if average >= 98 and average <= 100:
    equivalent = "1.0"
elif average >= 95 and average <= 97:
    equivalent = "1.25"
elif average >= 92 and average <= 94:
    equivalent = "1.5"
elif average >= 89 and average <= 91:
    equivalent = "1.75"
elif average >= 86 and average <= 88:
    equivalent = "2.0"
elif average >= 83 and average <= 85:
    equivalent = "2.25"
elif average >= 80 and average <= 82:
    equivalent = "2.5"
elif average >= 77 and average <= 79:
    equivalent = "2.75"
elif average >= 75 and average <= 76:
    equivalent = "3.0"
elif average < 75:
    equivalent = "5.0"  # Failure

print(f"Average:{round(average,2)}")
print(f"Equivalent:{equivalent}")

# if average >= 75:
#     result = "Passed"
# else:
#     result = "Failed"

# print(f"Average: {average}")
# print(f"Equivalent: {equivalent}")
# print(f"Status: {result}")


# Your average grade is ??