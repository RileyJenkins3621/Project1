n1 =int(input("Enter a number for the first list:  "))
n2=int(input("Enter a number for the first list:  "))
n3 =int(input("Enter a number for the first list:  "))
n4 =int(input("Enter a number for the first list:  "))
n5 =int(input("Enter a number for the first list:  "))
n6 =int(input("Enter a number for the second list:  "))
n7 =int(input("Enter a number for the second list:  "))
n8 =int(input("Enter a number for the second list:  "))
n9 =int(input("Enter a number for the second list:  "))
n10 =int(input("Enter a number for the second list:  "))
list1=[n1,n2,n3,n4,n5]
list2=[n6,n7,n8,n9,n10]
common_values=[]
for i in list1:
    if i in list2:
        common_values.append(i)

print(list1)
print(list2)
print(common_values)
