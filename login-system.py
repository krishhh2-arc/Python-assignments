def login_system():
    # Pre-defined user database
    database = {
        "admin": "admin123",
        "user1": "password123"
    }
    
    attempts = 3
    print("--- Login System ---")
    
    while attempts > 0:
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()
        
        if username in database and database[username] == password:
            print(f"Login Successful! Welcome, {username}.")
            return
        else:
            attempts -= 1
            print(f"Invalid username or password. Attempts remaining: {attempts}")
            
    print("Account locked due to too many failed attempts.")

if __name__ == "__main__":
    login_system()
  
