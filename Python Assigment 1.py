name = input("Enter your name = ")
father_Name = input("Enter your father name = ")
rollNO = input("Enter your Roll No = ")
mathMarks = int(input("Enter your Math Marks = "))
chemMarks = int(input("Enter your Chem Marks = "))
physicsMarks = int(input("Enter your Physics Marks = "))
urduMarks = int(input("Enter your Urdu Marks = "))
total_subjects = int (mathMarks+chemMarks+physicsMarks+urduMarks)
total_Marks = 400
total_Percentage = (total_subjects/400)*100
message = """
Student Name: {}
Father Name: {}
Roll NO: {}
Math Marks: {}
Chem Marks: {}
Physics Marks: {}
Urdu Marks: {}
Total Marks : {}
Marks in all Subjects: {}
Total Percentage: {}
"""
message1 = message.format(name, father_Name, rollNO, mathMarks, chemMarks, physicsMarks, urduMarks, total_Marks, total_subjects, total_Percentage)
print(message1)
