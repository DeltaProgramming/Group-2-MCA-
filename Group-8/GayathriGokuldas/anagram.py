s=input("Enter a string:")
r=sorted(s)
t=input("Enter another string:")
ts=sorted(t)
f=0
for i in r:
    if i in ts:
        f=0
    else:
        f=1
        break
if((len(s)==len(t)) and f==0):
    print("Anagram")
else:
    print("Not Anagram")
