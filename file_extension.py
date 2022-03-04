# Programme for printing file extension from the input file name

file_name = str(input("Enter the file name : "))
extension = file_name.split(".")
print("File extension : ", extension[-1])
input("Press any key to continue...")
