print("input: 'start' or 'stop' to command, and 'quit' to quit the game")
command = ""
started = False
while True:
    command = input("> ")
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started..")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped")
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand")
    
    
    