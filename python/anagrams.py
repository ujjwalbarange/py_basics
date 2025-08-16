a=list(input("1st word"))
b=list(input("2nd word"))
print(a)
print(b)
for i in a:
    if i in b:
        b.remove(i)
    else:
        print("Not an anagram")
        break
