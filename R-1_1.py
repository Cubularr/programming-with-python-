print("EXERCISE 1.1")

print("We will ask you to input a) a number that you want to check is a mutiple of b) a number")
print("Easy enough to understand: first number will have to be larger than the second")
x = int(input())
y = int(input())
def is_multiple(n, m):
    number = n/m
    if(number).is_integer():
        print("TRUE")
    else:
        print("FALSE")


is_multiple(x, y)
