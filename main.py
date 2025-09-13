def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def main():
    print("Welcome to the Calculator App!")
    print("Select function:")
    print("1 = Add")
    print("2 = Subtract")
    print("3 = Multiply")
    
    user_input = input("Enter your choice (1, 2, or 3): ")
    
    if user_input not in ['1', '2', '3']:
        print("Invalid choice. Please select 1, 2 or 3.")
        return
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if user_input == '1':
        print(f"The result is: {add(num1, num2)}")
    elif user_input == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif user_input == '3':
        print(f"The result is: {multiply(num1, num2)}")

if __name__ == "__main__":
    main()
