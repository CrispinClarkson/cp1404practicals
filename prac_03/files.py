# 1
output_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=output_file)
output_file.close()

