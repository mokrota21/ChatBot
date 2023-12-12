class Node:
    pass

class Node:
    """
    Node class represents nodes in conversation tree, each node has reply which is designed to be given when we get in this node,
    from each node we can go to next instance of conversation via key in neighbours, where keys are possible replies from user.
    Since we give reply when we get into node, we need root node to point to start of conversation (if we begin at start of conversation we don't print it)
    """
    def __init__(self, reply: list[str] =[''], root: bool = False, neg:Node = None) -> None:
        self.reply: list[str] = reply
        self.neighbours: dict[str, Node] = {}
        self.root: bool = root
        if neg is not None:
            self.neg = neg
        else:
            self.neg = self

    def set_neg(self, neg):
        self.neg = neg
    
    def __getitem__(self, key: str) -> Node:
        if self.root:
            assert len(self.neighbours) == 1
            return list(self.neighbours.values())[0]
        else:
            return self.neighbours.get(key, self.neg)
    
    def __setitem__(self, key: str, value: Node) -> None:
        # if node is root we want it to point only to one node
        if self.root:
            assert len(self.neighbours) <= 1
            if self.neighbours.keys():
                key = list(self.neighbours.keys())[0]
        self.neighbours[key] = value

class ConversationTree:
    """
    Class to store important info about conversation, it has root of the tree to be able to start conversation over,
    current node to keep track of our position
    """
    def __init__(self) -> None:
        self.root: Node = Node(root=True)
        self.now: Node = self.root
        self.path: list[Node] = [self.root]
        # self.attributes = {}
    
    def expand_answers(self, expansion) -> None:
        self.now.neighbours = expansion
    
    def leaf_now(self) -> bool:
        return len(self.now.neighbours) == 0

    def get_reply(self, key: str) -> None:
        self.now = self.now[key]
        self.path.append(self.now)

        reply = self.now.reply
        # reply = reply.format(**self.attributes)

        if self.leaf_now():
            self.reset()

        return reply
    
    def revert(self) -> None:
        assert len(self.path) >= 2
        self.now = self.path[-2]
        self.path.pop()

    def reset(self) -> None:
        self.now = self.root
        self.path = [self.root]