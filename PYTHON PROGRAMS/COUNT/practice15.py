#Count Vowels in a String
x=str(input("please enter any string."))
y=len(x)
print(y)
vowel=['a','e','i','o','u']
count=0
for i in x:
    if i in vowel:
        count=count+1


print(count)