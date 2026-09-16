def car_drive_simulation():
    started = False
    
    print("Type 'start', 'stop', or 'quit' to control the car.")
    
    while True:
        command = input("> ").strip().lower()
        
        if command == "start":
            if started:
                print("Car is already started!")
            else:
                started = True
                print("Car started... Ready to go!")
        elif command == "stop":
            if not started:
                print("Car is already stopped!")
            else:
                started = False
                print("Car stopped.")
        elif command == "quit":
            print("Exiting car drive simulation.")
            break
        else:
            print("I don't understand that command. Use 'start', 'stop', or 'quit'.")

if __name__ == "__main__":
    car_drive_simulation()
  
