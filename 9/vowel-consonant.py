with open("Story.txt", 'r') as file:
    content = file.read()
    
    vowel_count = 0
    consonant_count = 0
    lowercase_count = 0
    uppercase_count = 0
    character_count = 0
    
    for char in content:
        if char.isalpha():
            character_count += 1
            
            if char.lower() in "aeiou":
                vowel_count += 1
            else:
                consonant_count += 1
                
            if char.islower():
                lowercase_count += 1
            elif char.isupper():
                uppercase_count += 1
    
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)
    print("Number of lowercase letters:", lowercase_count)
    print("Number of uppercase letters:", uppercase_count)
    print("Total number of characters:", character_count)

