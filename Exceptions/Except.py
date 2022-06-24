while (True):
    try:
        n = float(input("Write a number: "))
        m = 4
        print("{} / {} = {}".format(n, m, n/m))
    except:
        print("There was an error, try again")
    else:
        print("Everything went alright")
        break
    finally:
        print("End of the iteration")