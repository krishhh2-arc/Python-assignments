def analyze_number(num):
    print(f"\n--- Analysis for Number: {num} ---")
    
    # Check Positive/Negative/Zero
    if num > 0:
        print("Status: Positive")
    elif num < 0:
        print("Status: Negative")
    else:
        print("Status: Zero")
        
    # Check Even/Odd
    if num != 0:
        if num % 2 == 0:
            print("Parity: Even")
        else:
            print("Parity: Odd")
            
    # Check Prime (for integers >= 2)
    if num > 1 and float(num).is_integer():
        num_int = int(num)
        is_prime = True
        for i in range(2, int(num_int ** 0.5) + 1):
            if num_int % i == 0:
                is_prime = False
                break
        print(f"Prime Number: {'Yes' if is_prime else 'No'}")

if __name__ == "__main__":
    try:
        user_input = float(input("Enter a number to analyze: "))
        analyze_number(user_input)
    except ValueError:
        print("Please enter a valid numeric value.")
      
