string_to_integer = int("10") #Converts a string to Int
print(f"A number: {string_to_integer}")

string_to_float = float("3.14159") #Converts a string to Float
print(f"A float number: {string_to_float}")

number_to_string = "A text and a number: " + str(10) + " " + str(3.14159) #Converts numbers to string
print(number_to_string)

binary_number = bin(15) #Converts numbers to binary
print(f"The number 15 is {binary_number} in binary system")

hex_number = hex(15) #Converts numbers to Hexadecimal
print(f"The number 15 is {hex_number} in hexadecimal")

binary_to_int = int("0b1111", 2)
print(f"The binary number 1111 is {binary_to_int}")

hex_to_int = int("0xf", 16)
print(f"The hexadecimal number f is {hex_to_int}")

absolute_value = abs(-15)
print(f"The absolute value of -15 is {absolute_value}")

rounded_number = round(14.6)
print(f"The number 14.6 rounded is {rounded_number}")

evaluation = eval("10 * 5")
print(f"The evaluation is {evaluation}")