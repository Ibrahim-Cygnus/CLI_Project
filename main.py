#Define the responses as functions
def greet(args):
     print("Hello")

def exit_program(args):
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
    user_input = input("Enter command: ").strip().lower()
    #Divide the input into pieces
    parts = user_input.split()
    #Prevent empty commands
    if not parts:
        continue
    #The first input piece is the function, and the rest are arguments
    command = parts[0]
    args = parts[1:]

    #Check if the entered command is listed
    if command in commands_n_responses:
        #Call the required functions and pass the arguments
        should_exit = commands_n_responses[command](args)
        if should_exit:
            break
    else:
        print("Invalid command. Please enter a valid command")
        continue