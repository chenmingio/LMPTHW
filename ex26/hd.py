import sys

# _, in_string = sys.argv

def string2hex(string):
    hex_list = [hex(ord(char))[2:] for char in string]
    # print(f">>> hex_list is {hex_list}.")
    return hex_list

def group_A(hex_list):
    list_1 = hex_list[:8]
    # print(f">>> list_1 is {list_1}.")
    list_2 = hex_list[8:]
    # print(f">>> list_2 is {list_2}.")
    return [list_1, list_2]

def print_hex_list(hex_list):
    for hex_num in hex_list:
        print(hex_num, end=' ')

def print_meta_list(hex_meta_list):
    for section in hex_meta_list:
        print_hex_list(section)
        print("\t", end='')
    tab_num = abs(8 - len(hex_meta_list[-1]))
    print("\t" * tab_num, end='')

def print_type_A(string):
    hex_list = string2hex(string)
    meta_list = group_A(hex_list)
    print_meta_list(meta_list)
    print(f"|{string}|")

