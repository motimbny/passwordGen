import random

global signs
signs=['-','+','[',',','?','#','@','!','&','%','*']

def selectCapLetter():
    return chr(random.randint(ord('A'),ord('Z')))
def selectLetter():
    return chr(random.randint(ord('a'), ord('z')))
def selectSign():
    return signs[random.randint(0,len(signs)-1)]
def selectNumber():
    return random.randint(0,10)
def shiftArr(arr,shift):
    for i in range(shift):
        temp = arr[len(arr)-1]
        for i in range(len(arr)-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
def createPassword(n,maxCap,maxSigns):
    password = [-1] * n
    flags = [0, 0]  # flags[0]=signs   flags[1]=Cap
    while -1 in password:
        j=random.randint(0,n-1)
        while password[j]!=-1:
            j=random.randint(0,n-1)
        if j%2==0 and flags[1]<maxCap:
            password[j]=selectCapLetter()
            flags[1]+=1
        elif j%3==0 and flags[0]<maxSigns:
            password[j]=selectSign()
            flags[0] += 1
        elif j<(n/2):
            password[j]=selectNumber()
        else:
            password[j]=selectLetter()
    return "".join(str(c) for c in password)


