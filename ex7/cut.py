import sys

while True:
    try:
        line = input()
    except EOFError:
        print(">>> EOFError found")
        sys.exit(0)
else:
    pass
    