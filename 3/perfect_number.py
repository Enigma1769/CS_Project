x= int(input("Enter the number: "))
l=[]
sum =0
for i in range(1,x):
    if x%i==0:
        sum+=i
if sum==x:
    print(f"{x} is a perfect number.")
else:
    print(f"{x} is not a perfect number")

