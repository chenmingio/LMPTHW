from tstree import TSTree


def test_set():
    names = TSTree()
    names.set("MM", "Mad MAX")
    names.set("OO", "YUAN YUAN")
    names.set("CM", "CHEN MING")
    names.set("CMO", "CHEN MING")
    names.set("CMOET", "CHEN MING")
    names.set("ZZ", "ZHI ZHANG")
    return names

def test_get():
    names = test_set()
    assert names.get("CM") == "CHEN MING"
    assert names.get("OO") == "YUAN YUAN"
    assert names.get("ZZ") == "ZHI ZHANG"
    assert names.get("MM") == "Mad MAX"
    assert names.get("LL") == None

def test_find_all():
    pass