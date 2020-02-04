- urlrouter
  - TSTree (tstree)
  - DoubleLinkedList (dllist)
  - BSTree (bstree)

- URLNode
    - init
        - key
        - val

- URLRouter
    - init
    - add
    - exact_match
    - best_match
        - match_all
    - match_all
    - match_shortest
        - match_all
    - match_longest
        - match_all

- TSTRouter
    - URLRouter
    - init
        - TSTree
    - add
        - TSTree.set
    - exact_match
        - TSTree.get
    - best_match
        - TSTree.find_part
    - match_all
        - TSTree.find_all

- DictRouter
    - URLRouter
    - init
        - dict
    - add
        - dict[]
        - URLNode
    - exact match
      - dict.get

- BSTreeRouter
    - URLRouter
    - init
        - BSTree
    - add
      - BSTree.set
    - exact_match
      - BSTree.get
    - _match_all
    - match_all
        - _match_all

- DListRouter

