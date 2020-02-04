from url import URLRouter


def test_set_get():
    URLHandler = URLRouter()
    URLHandler.set("/create/item/", "create item")
    URLHandler.set("/create/item/typeA/", "create item typeA")
    URLHandler.set("/create/item/typeB/", "create item typeB")
    URLHandler.set("/create/", "just create")
    URLHandler.set("/create/item/typeA/001/head", "create item typeA 001 head")
    URLHandler.set("/create/item/typeB/003", "create item typeB 003")

    assert URLHandler.search_exact("/create/item/") == "create item"
    return URLHandler

def test_search_all():
    URLHandler = test_set_get()
    result = [node.value for node in URLHandler.search_all("/create/item/")]
    print(result)

def test_search_best():
    URLHandler = test_set_get()
    assert URLHandler.search_best("/create/list") == "just create"
