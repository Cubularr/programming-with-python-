
aList = [1,3,0,2,6,8,3,7, 20, 1,235,23,8534,65]

def minmax(list1):
    try:
        for j in range(len(list1)):
            for i in range(len(list1)-1):
                if list1[i] > list1[i+1]:      
                    temporary = list1[i]           
                    list1[i] = list1[i+1]         
                    list1[i+1] = temporary
    except Exception:
        pass
    finally:
        print(list1)
        print("min = " + str(list1[0]))
        print("max = " + str(list1[-1]))
minmax(aList)
