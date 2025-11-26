def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("Simple Calculator CLI")
    print("Available operations: +, -, *, /")
    print("Type 'exit' to quit")
    
    while True:
        try:
            user_input = input("\nEnter calculation (e.g., 5 + 3): ").strip()
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format. Use: number operator number")
                continue
            
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator")
                continue
            
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    main()
