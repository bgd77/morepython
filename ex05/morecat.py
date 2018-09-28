import argparse

parser = argparse.ArgumentParser(description='Linux cat implementation written in Python')
parser.add_argument('files', type=argparse.FileType('r'), nargs='+',
    help="The files to be read")
parser.add_argument('-b', '--number-nonblank', action='store_true',
    help="Number nonempty output lines, overrides -n")
parser.add_argument('-E', '--show-ends', action='store_true',
    help="Display $ at end of each line")
parser.add_argument('-n', '--number', action='store_true',
    help="Number all output lines")
parser.add_argument('-s', '--squeeze-blank', action='store_true',
    help="Suppress repeated empty output lines")
parser.add_argument('-o', nargs=1, help="The file in which to print the output")
args = parser.parse_args()
\
def is_line_blank(line):
    if line.strip():
        return False
    else:
        return True

line_no = 1
previous_line_blank = False

def get_formated_line(line):
    global line_no
    global previous_line_blank

    if args.squeeze_blank:
        if previous_line_blank:
            if is_line_blank(line):
                return ''
            else:
                previous_line_blank = False
        elif is_line_blank(line):
            previous_line_blank = True

    if args.number or args.number_nonblank:
        if args.number_nonblank and is_line_blank(line):
            line = "\n"
        else:
            line = "\t{0:3}  {1}".format(line_no, line)
            line_no += 1

    if args.show_ends:
        line = line[:-1] + '$' + '\n'

    return line

if args.o is None:
    for file in args.files:
        for line in file:
            print(get_formated_line(line), end='')
else:
    with open(args.o[0], 'w') as output_file:
        for file in args.files:
            for line in file:
                output_file.write(get_formated_line(line))
