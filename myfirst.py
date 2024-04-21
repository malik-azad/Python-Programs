# EVEN OR ODD

def EvenOdd(n):
    if n % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")    
while(True):
    number = int(input("Enter the number to check whether even or odd "))
    EvenOdd(number)
