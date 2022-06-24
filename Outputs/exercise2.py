import sys
print(sys.argv)

row = int(sys.argv[1])
column = int(sys.argv[2])

if row >= 1 and row <= 9:
    if column >= 1 and column <= 9:
        for i in range(row):
            for j in range(column):
                print("*", end=" ")
            print()
