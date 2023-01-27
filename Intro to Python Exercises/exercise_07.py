exit=True 
this_list=[]
num_list=[]
while exit==True:
    s1 =input("Enter a word: ")
    if s1=="EXIT":
        exit=False
    this_list.append(s1)
print(this_list)
for item in this_list:
    for subitem in item.split():
        if(subitem.isdigit()):
            num_list.append(subitem)
print(num_list)
