# 1
output_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=output_file)
output_file.close()

# 2
input_file = open("name.txt", "r")
name = input_file.read().strip()
output_file.close()
print(f"Hi {name}!")

# 3
with open("numbers.txt", "r") as input_file:
    number1 = int(input_file.readline())
    number2 = int(input_file.readline())
print(number1 + number2)

# 4
total = 0
with open("numbers.txt", "r") as input_file:
    for line in input_file:
        number = int(line)
        total += number
print(total)



