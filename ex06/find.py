import os
import argparse
import fnmatch
import subprocess

parser = argparse.ArgumentParser(description='Linux find implementation written in Python')
parser.add_argument('path', type=str, default='.',
    help='The path where find will run')
parser.add_argument('-type', choices=['d', 'f'],
    help='Filter the search by directory or by file')
parser.add_argument('-name', type=str, help='File name pattern')
parser.add_argument('-print', action='store_true', help='Print the matches')
parser.add_argument('-exec', type=str,
    help='Run Linux command on matched files; only simple ls kind of works now')
args = parser.parse_args()

print(args)

files = list(os.scandir(args.path))

only_directories = True if args.type is not None and args.type == 'd' else False
only_files = True if args.type is not None and args.type == 'f' else False

for file in files[:]:
    if only_directories and file.is_file():
        files.remove(file)
        continue
    if only_files and file.is_dir():
        files.remove(file)
        continue
    if args.name is not None:
        if not fnmatch.fnmatch(file.name, args.name):
            files.remove(file)

files_full_path = [file.path for file in files]
files_full_path.sort()

if args.print:
    for file_path in files_full_path:
        print(file_path)

if args.exec:
    for file_path in files_full_path:
        subprocess.run([args.exec, file_path])
