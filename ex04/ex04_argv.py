import sys

def print_usage():
    print("Usage:")
    print(sys.argv[0] + " [-abc] [-text1 text] [-text2 text] [-number no] file")

user_arguments = sys.argv[1:]

if len(user_arguments) == 0 or user_arguments[0] == "-h":
    print_usage()
elif user_arguments[-1].startswith("-"):
    print("The last argument must be a file name")
    print_usage()

flags = ["-a", "-b", "-c"]
options = ["-text1", "-text2", "-number"]

filename = user_arguments[-1]
user_arguments.remove(filename)

for argument in user_arguments:
    if argument in flags:
        print("Running with flag " + argument)
        continue
    if argument in options:
        current_argument_index = user_arguments.index(argument)
        option_value = user_arguments[current_argument_index + 1]
        if option_value in flags or option_value in options or \
            option_value.startswith("-"):
            print("Option value not present for argument "+ argument)
        else:
            print("Argument " + argument + " with value " + option_value)
            del user_arguments[current_argument_index + 1]
            continue
    if not (argument in flags or argument in options):
        print("Argument " + argument + " not expected")

print("File name argument: " + filename)
