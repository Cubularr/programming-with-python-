import math


print("Exercise 1.4")

print("Please input a number")
print("This algorithm will take that number and find the sum of all the square numbers smaller than 'x'")
x = int(input("x = "))
list1 = []
finalResult = 0

def  sumOfSquares(num):
    global finalResult
    for i in range(num):
        if (math.sqrt(i)).is_integer():
            list1.append(i)
    print(list1)
    for j in range(len(list1)):
        finalResult += list1[j]
    print(finalResult)

    
sumOfSquares(x)
