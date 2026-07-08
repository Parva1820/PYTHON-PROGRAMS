#Palindrome Check Check whether a string or number is a palindrome.
x=str(input("enter any word: "))

if x==x[::-1]:
    print("YES, the given string is palindrome")
else:
    print("NO, the given string is not palindrome")