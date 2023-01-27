grade =int(input("Enter a grade between 0 to 100: "))
if(grade<=59):
    print("Your grade is F")
elif(grade>=60 and grade<=69):
    print("Your grade is D")
elif(grade>=70 and grade<=79):
    print("Your grade is C");
elif(grade>=80 and grade <=89):
    print("Your grade is B");
elif(grade>=90 and grade<=100 ):
    print("Your grade is A");
else:
    print("Please enter a number between 0 and 100")