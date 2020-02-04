import argparse
import re

# parser setting
def parse_arges():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', type=str, help="file path")
    parser.add_argument('-e', type=str, help="script")

    args = parser.parse_args()
    return 

def sed(args):
    filename = args.file
    pattern, replacement = args.e.split("/")[1:3]

    return (file_name, pattern, replacement)

def do_rep(file_name, pattern, replacement):
    p = re.compile(pattern)
    with open(filename) as f:
        for line in f.readlines():
            rc = p.sub(replacement, line)
            print(rc)

parse_arges()