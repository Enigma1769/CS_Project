def is_palindrome(number):
    num_str = str(number)
    if num_str == num_str[::-1]:
        return True
    else:
        return False

def is_armstrong(number):
    num_digits = len(str(number))
    sum_of_cubes = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** num_digits
        temp //= 10
    
    if sum_of_cubes == number:
        return True
    else:
        return False

while True:
    print("Menu:")
    print("1. Check if a number is a palindrome")
    print("2. Check if a number is an Armstrong number")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        number = int(input("Enter a number: "))
        if is_palindrome(number):
            print(number, "is a palindrome")
        else:
            print(number, "is not a palindrome")
    
    elif choice == '2':
        number = int(input("Enter a number: "))
        if is_armstrong(number):
            print(number, "is an Armstrong number")
        else:
            print(number, "is not an Armstrong number")
    
    elif choice == '3':
        print("Exiting the program...")
        break
    
    else:
        print("Invalid choice. Please enter a valid choice (1-3).")