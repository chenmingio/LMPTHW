import tr

def test_tr():
    string = "chenminghellloworld"
    result = tr.tr(string, 'l', 'xxx')
    # print(f">>> result is {result}.")
    assert result == "chenminghexxxxxxxxxoworxxxd"

def test_main():
    result = tr.main(['arg1', 'arg2', 'argv3'])
    print(f">>> result is {result}.")
