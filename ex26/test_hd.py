import hd


def test_string2hex():
    hd.string2hex("Hello There")
    hd.string2hex("WTF is this?")

def test_group_A():
    hex_list = hd.string2hex("Hello There.")
    assert hd.group_A(hex_list) == [['48', '65', '6c', '6c', '6f', '20', '54', '68',],['65', '72', '65', '2e']]

def test_print_hex_list():
    hex_list = hd.string2hex("Hello There.")
    hd.print_hex_list(hex_list)
    hex_list2 = hd.string2hex("WTF is this?")
    hd.print_hex_list(hex_list2)

def test_print_type_A():
    print("\n")
    hd.print_type_A("Hello There.")
    hd.print_type_A("WTF is this?")
    hd.print_type_A("Chen Ming is the boss")
