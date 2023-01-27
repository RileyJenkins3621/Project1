def isSuffix(s1, s2):
     
    n1 = len(s1)
    n2 = len(s2)
    if (n1 > n2):
        return False
    for i in range(n1):
        if(s1[n1 - i - 1] != s2[n2 - i - 1]):
            return False
    return True
 
if __name__ == "__main__":
     
    s1 = "brush"
    s2 = "paintbrush"
 
    result = isSuffix(s1, s2)
 
    if (result): 
        print("Yes")
    else:
        print( "No")
 