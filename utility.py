# -- convert input into positive integers
def convert_to_int(message):
    converted_input = None
    while converted_input == None:
        raw_message = input(message)
        keyword_check(raw_message)
        try:
            converted_input = int(raw_message)
            if converted_input < 0:
                print("Input cannot be a negative integer...try entering a positive whole number(integer)")
                converted_input = None
        except:
            print("Input not recongnized...try entering a positive whole number(integer)")
    return converted_input
# -- check for quit message
def keyword_check(raw_message):
    if raw_message == "q" or raw_message == "quit" or raw_message == "quit()" or raw_message == "exit" or raw_message == "exit()":
        print(" <<< Game Exited >>>")
        quit()
# -- function used to clear screen
def push_screen(number):
    if number < 0:
        number = 1
    for i in range(number):
        print()
