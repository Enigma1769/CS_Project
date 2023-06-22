def ftemp(a):
    fahrenite = ((a*9)/5)+32
    return fahrenite

x=int(input("Enter the temperature in celsius: "))
print("The temperatue in fahrenite is :-",ftemp(x))