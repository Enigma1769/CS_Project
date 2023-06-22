
def countwords():
    characters=[]
    f= open("Quotes.txt","r")
    for i in f:
        while i.is_alnum():
            if i.is_alpha():
                characters.append(i)
    print(characters)


countwords()
