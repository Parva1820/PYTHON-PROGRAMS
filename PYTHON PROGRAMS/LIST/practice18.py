#Remove Duplicates from a List
names=["parva","priyanshu","priyanshu","meet","parva","rushiraj"]
unique = []

for i in names:
    if i not in unique:
        unique.append(i)

print(unique)