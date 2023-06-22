with open('MyNotes.txt',"r") as file:
    data = file.readlines()
    for line in data:
        if line[0].lower()=='g':
            print(line)
