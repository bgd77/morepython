import re
import argparse

parser = argparse.ArgumentParser(description='Basic Linux grep implementation written in Python')
parser.add_argument('pattern', type=str, help="The pattern to be used")
parser.add_argument('files', type=argparse.FileType('r'), nargs='+',
    help="The files to be read")
parser.add_argument('-i', '--ignore-case', action='store_true',
    help="Ignore case in pattern")
parser.add_argument('-v', '--invert-match', action='store_true',
    help="Invert the sense of matching, to select non-matching lines.")
parser.add_argument('-c', '--count', action='store_true',
    help="Suppress normal output; instead print a count of matching lines for \
    each input file.  With the -v, --invert-match option, count non-matching lines.")
parser.add_argument('-o', '--only-matching', action='store_true',
    help="Print only the matched (non-empty) parts of a matching line, with \
    each such part on a separate output line.")
args = parser.parse_args()

if args.ignore_case:
    re_pattern = re.compile(args.pattern, re.IGNORECASE)
else:
    re_pattern = re.compile(args.pattern)

def should_print_line(line_matched):
    if line_matched and not args.invert_match:
        return True
    elif not line_matched and args.invert_match:
        return True
    else:
        return False

for file in args.files:
    file_lines = file.readlines()
    line_count = 0
    for line in file_lines:
        if args.only_matching and not args.count:
            matches = re_pattern.findall(line)
            if matches:
                for match in matches:
                    print(file.name + ':' + match)
        else:
            match = re_pattern.search(line)
            if should_print_line(match is not None):
                if args.count:
                    line_count += 1
                else:
                    print(file.name + ':' + line, end='')
    if args.count:
        print(file.name + ':' + str(line_count))
