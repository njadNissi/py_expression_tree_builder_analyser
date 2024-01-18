from binary_node import BNode
import conversor as conv


class BTree:

    def __init__(self, root: BNode):
        self.root = root
        self.HEIGHT = self.__height(self.root)
        self.nodes_dlr = []
        self.nodes_ldr = []
        self.nodes_lrd = []
        self.nodes_layer = []
    
    @staticmethod
    def from_postfix(postfix: list) -> BNode:
        
        tree = BTree(root=BTree.build(postfix))
        
        return tree.root


    @classmethod
    def class_method_ex(cls, args):
        pass


    @staticmethod
    def from_infix(infix: list) -> BNode:

        tree = BTree(root=BTree.build(infix))
        
        return tree.root


    def insertLeftChild(self, parent, child):
        parent.left = child


    def insertRightChild(self, parent, child):
        parent.right = child


    def delete(Self, node):
        pass


    @staticmethod
    def build(postfix: list) -> BNode:

        stack = []

        for e in postfix:
            
            node = BNode(e)
            
            if e in conv.Operators: # an operator case

                node.set_children(rchild=stack.pop(), lchild=stack.pop()) # a root node

            stack.append(node)

        return stack.pop() # the Root of the tree
    

    def DLR(self):
        """
            First-Order Traversal: 
                D:root => L:left-child => R:right-chid
        """
        self.__dlr(self.root)
        return self.nodes_dlr


    def __dlr(self, root):
        self.nodes_dlr.append(root.data)
        if root.left != None:
            self.__dlr(root.left)
        if root.right != None:
            self.__dlr(root.right)


    def LDR(self):
        """
            In-Order Traversal: 
                L:left-child => D:root => R:right-chid
        """
        return self.__ldr(self.root)


    def __ldr(self, root):
        if root.left != None:
            self.__ldr(root.left)

        self.nodes_ldr.append(root.data)

        if root.right != None:
            self.__ldr(root.right)
        return self.nodes_ldr

    def LRD(self):
        """
            Post-Order Traversal: 
                L:left-child => R:right-chid => D:root
        """
        self.__lrd(self.root)
        return self.nodes_lrd


    def __lrd(self, root):
        if root.left != None:
            self.__lrd(root.left)

        if root.right != None:
            self.__lrd(root.right)

        self.nodes_lrd.append(root.data)


    def Layer(self):
        for i in range(1, self.HEIGHT + 1):
            self.__layer(self.root, i)

        return self.nodes_layer


    def __layer(self, root, level):
        if root is None:
            return
        if level == 1:
            self.nodes_layer.append(root)
        else:
            self.__layer(root.left, level-1)
            self.__layer(root.right, level-1)


    def __height(self, node: BNode):
        """
            Compute the height of a tree--the number of nodes
            along the longest path from the root node down to
            the farthest leaf node
        """
        if node is None:
            
            return 0

        else:

            # Compute the height of each subtree
            lheight = self.__height(node.left)
            rheight = self.__height(node.right)

            # Use the larger one
            if lheight > rheight:

                return lheight+1
            
            else:
                
                return rheight+1	


"""
# t = BTree('36+54*-3-873-*2/+1+93/-2')
t = BTree('36+54*-')
tg = []
for n in t.nodes:
    s = '     ' + str(n.data) + '\n'
    if n.left:
        s += ' ' + str(n.left.data) + '\n'
    if n.right:
        s += '         ' + str(n.right.data) + '\n'
    s += '-'*50

    tg.append(s)

for layer in tg[::-1]:
    print(layer)
"""