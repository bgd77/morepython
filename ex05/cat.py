import argparse

parser = argparse.ArgumentParser(description='Linux cat implementation written in Python')
parser.add_argument('files', type=argparse.FileType('r'), nargs='+', help="The files to be read")
parser.add_argument('-o', nargs=1, help="The file in which to print the output (optional)")
args = parser.parse_args()

if args.o is None:
    for file in args.files:
        print(file.read(), end='')
else:
    with open(args.o[0], 'w') as output_file:
        for file in args.files:
            output_file.write(file.read())
