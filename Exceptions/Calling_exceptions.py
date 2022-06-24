def my_function(number = None):
    try:
        if number is None:
            raise ValueError("ERROR!, there can't be none value")
    except ValueError:
        print("ERROR!, there can't be none value")

my_function()