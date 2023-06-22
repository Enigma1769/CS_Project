
def countwords(file_name):
    try:
        with open(file_name, 'r') as file:
            r = file.read()
            words = r.split()
            print("Total number of words:", len(words)) 
            print("Total number of characters:", len(r))
    except FileNotFoundError:
        print("File not found.")

#driver code 
countwords("Quotes.txt")