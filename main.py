
# Practical No: 03
# Program to Write and Append Data to a File

# Writing data into a file
file = open("student.txt", "w")
file.write("Name: Jariab Noor Salam\n")
file.write("Roll: 356537\n")
file.write("Department: Computer Technology\n")
file.close()

# Appending data to the file
file = open("student.txt", "a")
file.write("Semester: 3rd\n")
file.write("Institute: National Institute of Technology\n")
file.close()

# Reading data from the file
file = open("student.txt", "r")
print("File Contents:")
print(file.read())
file.close()
