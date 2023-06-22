def count_wh():
    w=h=0

    with open('Country.txt', 'r') as file:
        data= file.readlines()
        for line in data:
            if line[0].lower() =='w':
                w+=1
            if line[0].lower() =='h':
                h+=1
        
    return w,h
w,h=count_wh()
print("The no of w in the file are :",w)
print("The no of h in the file are :",h)