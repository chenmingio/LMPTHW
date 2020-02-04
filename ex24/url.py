from tstree import TSTreeNode, TSTree

class URL(TSTreeNode):
    pass

class URLRouter(TSTree):

    def set(self, url_string, action):
        urls = url_string.split('/')[1:-1]
        # print("urls to set :", urls)
        super().set(urls, action)

    def search_exact(self, url_string):
        urls = url_string.split('/')[1:-1]
        return super().get(urls)

    def search_best(self, url_string):
        urls = url_string.split('/')[1:-1]
        node = self._search_best(self.root, urls)
        return node and node.value or None

    def _search_best(self, node, keys):
        key = keys[0]

        if not node:
            return node

        if key < node.key:
            return self._search_best(node.low, keys)
        elif key == node.key:
            if len(keys) > 1:
                return self._search_best(node.eq, keys[1:])
            else:
                return node
        else:
            return self._search_best(node.high, keys)

    def search_all(self, url_string):
        urls = url_string.split('/')[1:-1]
        return super().find_all(urls)


    def search_shortest(self, parameter_list):
        pass

    def search_longest(self, parameter_list):
        pass
