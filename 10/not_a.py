with open("file.txt","r") as file, open("new_file.txt","w") as newfile :
    content = file.readlines()
    for i in content:
        if 'a' not in i:
            newfile.write(i)
