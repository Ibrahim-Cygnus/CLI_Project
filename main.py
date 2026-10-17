#Define the responses as functions
def greet():
     print("Hello")

def exit_program():
     print("Goodbye")
     return True

#The list of valid commands and their responses
commands_n_responses = {
    "greet": greet,
    "exit" : exit_program
}
#the main infinite loop
while True:
    #Input from user, cleaned and formatted
    command = input("Enter command: ").strip().lower()
    #If command is empty, go again.
    if not command:
        continue
    #Check if the entered command is listed
    if command in commands_n_responses:
        #Respond to command
        should_exit = commands_n_responses[command]()
        if should_exit:
            break

    else:
        print("Invalid command. Please enter a valid command")
        continue