import sys

def main(argv):
    return(argv[1:])

def tr(string, old, new):
    return(string.replace(old, new)) 


if __name__ == "__main__":
    main(sys.argv)