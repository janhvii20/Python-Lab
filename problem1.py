f=open("f1.txt","r")
i=0
j=0
for x in f :
    for y in x: 
     if y.isalnum():
        i+=1
     if y.isalpha():
        j+=1
print("total letter",j)
print("total num",i)