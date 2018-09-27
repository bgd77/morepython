import argparse

parser = argparse.ArgumentParser(description='Parser for exercise 04 using argparse')
parser.add_argument('-a', help="Flag -a", action='store_true')
parser.add_argument('-b', help="Flag -b", action='store_true')
parser.add_argument('-c', help="Flag -c", action='store_true')
parser.add_argument('-text1', help="Option -text1")
parser.add_argument('-text2', help="Option -text2")
parser.add_argument('-number', help="Option -number", type=int)
parser.add_argument('file', type=argparse.FileType('r'), help="File name")


args = parser.parse_args()
print(args)
