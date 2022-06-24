import sys

if len(sys.argv) == 2:
    number = int(sys.argv[1])
    if number > 0 and number < 10000:
        number_string = str(number)
        number_length = len(number_string)
        
        for i in range(number_length):
            print("{:04d}".format(int(number_string[number_length-1-i]) * 10 ** i))

    else:
        print("Error - Number is not valid")
        print("Example: exercise3.py [0 - 9999]")

else:
    print("Error - Invalid arguments")
    print("Example: exercise3.py [0 - 9999]")

input("Press ENTER to exit")