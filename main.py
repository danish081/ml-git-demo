def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Welcome to the Calculator App!")
    print("Select function:")
    print("1 = Add")
    print("2 = Subtract")
    
    user_input = input("Enter your choice (1 or 2): ")
    
    if user_input not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if user_input == '1':
        print(f"The result is: {add(num1, num2)}")
    elif user_input == '2':
        print(f"The result is: {subtract(num1, num2)}")

if __name__ == "__main__":
    main()
