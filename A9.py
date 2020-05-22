

num = input("enter a value to check for palindrome ")

a = num[::-1]
print(a)

if num == a :
    print("Value is palindrome :)")
else :
    print("Value isn't a palindrome :(")