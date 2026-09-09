name = input("Enter student name:")
python = int(input("Enter Python marks:"))
math = int(input("Enter math marks:"))
Data_Science = int(input("Enter DS marks:"))
Data_Analysis = int(input("Enter DA marks:"))
Devops = int(input("Enter devops marks:"))
total = python + math + Data_Science + Data_Analysis + Devops
percentage = (total/500) * 100
if percentage >= 90:
    grade = "A"
elif percentage >= 80 :
    grade = "B"
elif percentage >= 70 :
    grade = "C"
elif percentage >= 60 :
    grade = "D"
else:
    grade = "F"

if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"


print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)