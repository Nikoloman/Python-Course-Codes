import sys

if len(sys.argv) == 3:
    text = sys.argv[1]
    repeatations = int(sys.argv[2])

    for r in range(repeatations):
        print(text)
else: 
    print("Error - Introduce valid arguments")
    print("Example: write_lines.py \"Text\" 5")