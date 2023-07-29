from student import*
def makeStudent(Strform):
    name,hours,qpoints=Strform.split()
    return Student(name,hours,qpoints)

# open the input file for reading
filename = input("Enter the name of the grade file: ")
infile = open(filename, 'r')

# set best to the record for the first student in the file
best_gpa = 0
best_students = []
#first_line = True

# process subsequent lines of the file
for line in infile:

    # turn the line into a student record
    student = makeStudent(line)

    # check if this student is the best so far
    student_gpa = student.gpa()
    if student_gpa > best_gpa:
        best_gpa = student_gpa
        best_students = [student]
        #first_line = False
    elif student_gpa == best_gpa:
        best_students.append(student)

infile.close()

# print information about the best students
print("The best students are:")
for student in best_students:
    print(student.getName())
    print("hours:", student.getHours())
    print("GPA:", student.gpa())
