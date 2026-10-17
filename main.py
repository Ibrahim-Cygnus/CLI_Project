#The list of valid commands and their responses
commands_n_responses = {
    "greet": "Hello"
}
#the main infinite loop
while True:
    #Input from user
    command = input("Enter command: ").lower()
    #Check if the entered command is listed
    if command in commands_n_responses:
            print(commands_n_responses[command])
    else:          
        #Exit command that terminates the loop
        if command == "exit":
            print("Goodbye")
            break
        #Prevent user error
        else:
            print("Invalid command. Please enter a valid command")
            continue