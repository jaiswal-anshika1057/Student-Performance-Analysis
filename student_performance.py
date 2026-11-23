# Student Performance Analysis System
print("Welcome to STUDENT Performance Analysis System")
name = input ("Enter Student Name:")
dbms = float (input("Enter Dbms Marks: "))
python = float(input("Enter Python Marks: "))
maths = float(input ("Enter Maths Marks: "))
total = dbms + python + maths 
percentage = total / 3
print("\n------ STUDENT RESULT ------")
print("Student Name:", name)
print("Total Marks:", total, "/300")
print("percentage:", percentage, "%")
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D" 
else:
    grade = "Fail"
print("Garde:", grade)

