import argparse
import sys

parser = argparse.ArgumentParser(description='Basic Linux cut implementation written in Python')
parser.add_argument('-file', type=str,
    help="The file to be used. If not present, stdin is read")
parser.add_argument('-d', '--delimiter', type=str, help="Field delimiter")
parser.add_argument('-f', '--fields', type=str,
    help="Select only these fields;  also print any line that contains no delimiter character")

args = parser.parse_args()

delimiter = args.delimiter

def get_start_end_fields(required_fields):
    # The fields should be in one of the formats (all cases include that field):
    # 1) N -> get Nth field
    # 2) N- -> from N field to end
    # 3) N-M -> from N field to M fields
    # 4) -M -> from start to N field
    if '-' in required_fields:
        if required_fields.startswith('-'):  # case 4)
            return 0, int(required_fields[1:])
        elif required_fields.endswith('-'):  # case 2)
            return int(required_fields[:required_fields.index('-')]), None
        else:  # case 3)
            delim_index = required_fields.index('-')
            return int(required_fields[:delim_index]), int(required_fields[delim_index + 1:])
    else:  # case 1)
        return int(required_fields), int(required_fields)

def print_delimited_line(delimited_line, start_field, end_field):
    if end_field == None:
        end_field = len(delimited_line)
    for element in range(start_field - 1, end_field):
        print(delimited_line[element], end=' ')
    print()

start_field, end_field = get_start_end_fields(args.fields)

if args.file is None:
    for line in sys.stdin:
        if line.startswith('total'):
            continue
        if delimiter in line:
            delimited_line = line.split(delimiter)
            print_delimited_line(delimited_line, start_field, end_field)
        else:
            print(line)
else:
    pass
