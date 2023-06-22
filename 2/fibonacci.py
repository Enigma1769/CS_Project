first=0
second=1
temp=0

x=int(input("How many iterations do you want (>2)"))
print(first,second,end=" ")
for i in range (2,x):
    temp = first+second
    first = second
    second= temp
    print(temp,end=" ")

