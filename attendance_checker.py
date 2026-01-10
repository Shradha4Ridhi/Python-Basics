# Student Attendance Checker

total_classes = int(input("Enter total number of classes: "))

attended_classes = int(input("Enter number of classes attended: "))

attendance_percentage = (attended_classes / total_classes) * 100

     print("Attendance Percentage:", attendance_percentage)

if attendance_percentage >= 75:
      print("You are eligible to attend exams.")
else:
      print("You are NOT eligible to attend exams.")
