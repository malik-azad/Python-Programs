
def findGreaterNumber(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both Number are equal" 

    num1 = int(input("Enter the first number")) 
    num2 = int(input("Enter the second number"))
    greatestNumber = findGreaterNumber(num1, num2)
    print("The greater number is: ", greatestNumber)       