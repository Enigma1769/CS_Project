def count_wh():
    count = 0

    with open('Country.txt', 'r') as file:
        data= file.readline()
        for line in data:
            if line[0].lower() in ['w','h']:
                count+=1

    return count
print(count_wh())