n1 =int(input("Enter integer "))
n2=int(input("Enter integer "))
n3 =int(input("Enter integer "))
n4 =int(input("Enter integer "))
n5 =int(input("Enter integer "))
n6 =int(input("Enter integer "))
n7 =int(input("Enter integer "))
n8 =int(input("Enter integer "))
n9 =int(input("Enter integer "))
n10 =int(input("Enter integer "))
list1=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
two_values=[]
for i in list1:
    x=list1.count(i)
    if x==2:
        two_values.append(i)
for i in two_values:
     x=two_values.count(i)
     if x>1:
       del two_values[i]

print(two_values)

