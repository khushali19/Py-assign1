
a = int(input("Enter starting point: "))
b = int(input("Enter the ending point: "))



for n in range(a,b) :

    if(n==1): continue

    flag = 1

    for val in range(2, n//2 +1):
        if(n%val == 0):
            flag=0
            break

    if(flag==1):
        print("Prime number: ",n)
