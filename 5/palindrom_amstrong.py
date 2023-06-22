def is_palindrome(number):
    num_str = str(number)
    if num_str == num_str[::-1]:
        return True
    else:
        return False

def is_armstrong(number):
    power_sum=0
    num_str = str(number)
    num_digits = len(str(number))
    for i in range (num_digits):
        power_sum+= int(num_str[i])**num_digits
    if power_sum == number:
        return True
    else:
        False


while True:
    print("\n\n")
    print("Menu:")
    print("1. Check if a number is a palindrome")
    print("2. Check if a number is an Armstrong number")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        number = int(input("Enter a number: "))
        print()
        if is_palindrome(number):
            print(number, "is a palindrome")
        else:
            print(number, "is not a palindrome")
    
    elif choice == '2':
        number = int(input("Enter a number: "))
        print()
        if is_armstrong(number):
            print(number, "is an Armstrong number")
        else:
            print(number, "is not an Armstrong number")
            
    
    elif choice == '3':
        print()
        print("Exiting the program...")
        break
    
    else:
        print()
        print("Invalid choice. Please enter a valid choice (1-3).")