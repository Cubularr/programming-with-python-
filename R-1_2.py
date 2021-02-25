print("EXERCISE 1.2")

print("THe last printed message of this function shows whether or ot the number is false")

def is_even(k):
    string = str(k)
    for element in string:
        if element == ("2" or "4" or "6" or "8" or "0"):
            print("TRUE")
        else:
            print("FALSE")
is_even(15643278042)
