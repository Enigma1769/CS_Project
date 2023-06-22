#To write a Python Program to Read a text file "Story.txt" line by line and display each word separated by '#'.
file=open("Story.txt","r")
read=file.readlines()
for line in read:
    linewords = line.split()
    for word in linewords:
        print(word,end="#")