myList = [ 'kupwara','baramulla','srinagar',9,5,1, True, 2.34]

l1=[]
l2=[]

for item in myList:
    if type(item) == str:
        l1.append(item)
    elif type(item) == int:
        l2.append(item)
    else:
        pass
             
print(myList)
print(l1)
print(l2)