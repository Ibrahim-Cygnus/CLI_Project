#Utilize external files
from state import AvailabilityOfData
import data_handler
#We need a global variable to store the loaded data in it so that we use it in different functions
sample_data = None
state = AvailabilityOfData()    
#Define the responses as functions
def help(args, state):
    print("Available commands are:")
    for cmd in commands_n_responses:
        print(f'{cmd}. Example use:- {commands_n_responses[cmd][1]}')
        
def greet(args, state):
     print("Hello")

def exit_program(args, state):
     print("Goodbye")
     return True

def load(args, state):
    state.data = data_handler.load_file(args[0])
    if state.data:
        print(f'Data loaded successfully. Rows:{len(state.data)}')
    else:
        print("An error has occurred. Please try again")

def show(args, state):
    if not state.data:
        print("show what?")
    else:
        for row in state.data:
            print(row)

def filter_function(args, state):
    if not state.data:
        print("No data loaded, please load data first")
        return None
    elif len(args) != 3:
        print("Invalid arguments for the command filter")
        return None
    filtered_data = data_handler.filter_data(args, state.data)
    if not filtered_data:
        print("No matches")
        return None
    print(filtered_data)

def average(args, state):
    if len(args) != 1:
        print("Invalid arguments for the command average")
        return None
    if not state.data:
        print("No data loaded, please load data first")
        return None
    try:
        int(state.data[0][args[0]])
        average_data = data_handler.average_field(args[0], state.data)
        print(average_data)
    except ValueError:
        print(f'You can\'t average {args[0]}')
    except KeyError:
        print(f'No such field as {args[0]}')

def max(args, state):
    if not state.data:
        print("No data loaded, please load data first")
        return None
    if len(args) != 1:
        print("Invalid arguments for the command max")
        return None
    try:
        int(state.data[0][args[0]])
        maximum = data_handler.maximum(args[0], state.data)
        print(maximum)
    except ValueError:
        print(f'This command does not apply to {args[0]}')
    except KeyError:
        print(f'No such field as {args[0]}')

def find(args, state):
    if not state.data:
        print("No data loaded, please load data first")
        return None
    if len(args) != 2:
        print("Invalid arguments for the command find")
        return None
    try:
        search = data_handler.finder(args[0], args[1], state.data)
        if not search:
            print("No matches")
            return None
        print(search)
    except KeyError:
        print(f'No such field as {args[0]}')
        
#The list of valid commands and their responses
commands_n_responses = {
    "greet": [greet, "greet"],
    "exit" : [exit_program, "exit"],
    "load" : [load, "load <file_name.with_extension>"],
    "show" : [show, "show"],
    "filter" : [filter_function, "filter <field> <operator> <criterion>. For example: filter age < 20"],
    "average" : [average, "average <field>. For example: average score"],
    "max" : [max, "max <field>. For example: max score"],
    "find" : [find, "find <field> <value>. For example: Find name sara"],
    "help" : [help, "help"]
}
#The main infinite loop
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
        should_exit = commands_n_responses[command][0](args, state)
        if should_exit:
            break
    else:
        print("Invalid command. Please enter a valid command")
        continue