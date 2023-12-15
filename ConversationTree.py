class Node:
     pass

class Node:
        """ 
        Node need to contain reply (string template) and links to adjacent nodes (dictionary). Since user can give any reply
        there is also link to negative node, this nodes is used when user give not determined by code reply, 
        by default it's node itself.
        """
        def __init__(self, reply: list[str] = [], neg: Node = None):
            self.reply = reply
            self.adj: dict[str, Node] = {}
            if neg is None:
                 neg = self
            self.neg = neg

        # Method to get neighbours
        def __getitem__(self, key):
            return self.adj.get(key, self.neg)

        # Method to set neighbours
        def __setitem__(self, key, val: Node):
            self.adj[key] = val
            val.adj['back'] = self
        
        # Method to set negative node
        def set_neg(self, neg: Node):
            self.neg = neg
            neg.adj['back'] = self

class ConversationTree:
        """
        Tree itself, stores root, current node and path. Contains some utility methods such as revert, reset etc. The most important is get_answer. It
        takes user message and calculated where to go in conversation tree, when we get in the new node we send message stored in it to the user. Because
        of this we need root node to be empty, otherwise we lose initial message
        """
        def __init__(self, start: Node) -> None:
             self.root = Node()
             self.root.set_neg(start)

             self.now = self.root
             self.path = [self.root]

        # Method to check if we are in a leaf
        def leaf(self):
             return len(self.now.adj) == 1
        
        # Method to revert to previous state in conversation tree. Since it's pseudocode I dont look at every case and it can be wrong
        def revert(self):
             self.now = self.path[-2]
             self.path.pop()
        
        # Method to restart conversation
        def restart(self):
             self.now = self.root
             self.path = [self.root]

        # Method to get reply given user message. Attribute is dictionary of some attributes such as username, name of the channel, date etc. In our code
        # we store only last reply and username. If we are in leaf it means we write final message and want to restart
        def get_answer(self, reply: str, attributes: dict[str, str]):
             current = self.now[reply]

             messages = list(map(lambda message: message.format(**attributes), current.reply))
             self.now = current

             if self.leaf():
                  self.restart()
            
             return messages
