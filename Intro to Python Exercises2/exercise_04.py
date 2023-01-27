sum=0
count=0
while count <5:
    try:
        num=int(input("Enter int #{} ".format(count +1) ))
        sum+=num
        count +=1
    except ValueError:
        print("Invalid input. Please enter an integer.")
print("Your sum is ", sum)
    
