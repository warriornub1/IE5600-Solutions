list1 = input('Enter a list of string values: ').split()
list2 = input('Enter another list of string values: ').split()

list3 = []
lengthList1 = len(list1)
lengthList2 = len(list2)
longerLength = lengthList1 if lengthList1 > lengthList2 else lengthList2

for i in range(longerLength):
    
    leftString = list1[i] if i < lengthList1 else ''
    rightString = list2[i] if i < lengthList2 else ''
    
    list3.append(leftString + rightString)

print(list3)
