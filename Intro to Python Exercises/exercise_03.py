def sum(x):
    sum=0
    for i in x:
        sum=sum+int(i)**3
    return sum
cubed =(input("Enter a positive integer: "))
print(sum(cubed))