f=open("f2.txt","r")
i=0
j=0
for x in f:
    for y in x:
        if y.isupper():
            i+=1
        if y.islower():
            j+=1
print("capital letter",i)
print("lower letter",j)