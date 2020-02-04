import argparse
from pathlib import Path

# parser setting
parser = argparse.ArgumentParser()

parser.add_argument('path', type=str, help="path to find", nargs='+')
parser.add_argument('--part', type=str, help="part number. support partically matching")
parser.add_argument('--type', type=str, help="search pdf/xlsx/etc...")
parser.add_argument('--print', action='store_true')

args = parser.parse_args()
print(args)

root = "V:\\Purchasing\\00 Purchasing New Folder\\12 GE Pur. - Program Purchasing\\01 Components - HSE\\03 Program Purchasing_APS_Chen Ming\\"
p = Path(root + ' '.join(args.path))
print(">>> path is :", p)

if args.part:
    if args.type:
        target = "*" + args.part + "*" + args.type
        print(">>> target is: ", target)
        rc = Path(p).rglob(target)
        for in_file in rc:
            print(in_file.name)
    else:
        target = "*" + args.part + "*.*"
        rc = Path(p).rglob(target)
        for in_file in rc:
            print(in_file.name)
else:
    pass
