#Find Frequency of Each Character in a String
x=str(input("ENTER ANY STRING"))
freq={}
for ch in x:
    if ch in freq:
        freq[ch]+=1

    else:
        freq[ch]=0

print(freq)