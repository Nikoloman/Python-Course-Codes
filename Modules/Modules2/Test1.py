def function():
    print("Hey There!")

class Test():
    def __init__(self) -> None:
        print("An instance of 'Test' has been created")

if __name__ == "__main__": #Checks if it's the main script, if yes, it'll execute the lines without opening in the other script1
    function()
    Test()
    print("Test1.py name -->", __name__)