from binary_node import BNode
import exprParser as parser


class BTree:

    def __init__(self, root: BNode):
        self.root = root
        self.__ldr = [] # nodes after preorder traversal
        self.__ldr = [] # nodes after inorder traversal
        self.__lrd = [] # nodes after postorder traversal
        self.__layer = [] # nodes after layerorder traversal

    
    @staticmethod
    def from_postfix(postfix: list):
        
        tree = BTree(root=BTree.build(postfix))
        
        return tree


    @classmethod
    def class_method_ex(cls, args):
        pass


    @staticmethod
    def from_infix(infix: list):
        
        tree = BTree(root=BTree.build(parser.infixToPostfix(infix)))
        
        return tree


    def insertLeftChild(self, parent, child):
        parent.left = child
        self.height = self.__height(self.root)


    def insertRightChild(self, parent, child):
        parent.right = child
        self.height = self.__height(self.root)


    def delete(self, node):
        self.height = self.__height(self.root)


    @staticmethod
    def build(postfix: list) -> BNode:

        stack = []

        for e in postfix:
            
            node = BNode(e)
            
            if e in parser.Operators: # an operator case

                node.set_children(rchild=stack.pop(), lchild=stack.pop()) # a root node

            stack.append(node)

        return stack.pop() # the Root of the tree
    

    """
        The methods below are called by default while instantiating this class
        Do call them manually after dynamic operations(insertion, deletion) to updated data
    """
    @property
    def prefix(self):
        """
            First-Order Traversal: 
                D:root => L:left-child => R:right-chid
        """
        self.__preorder_traveral(self.root)

        return self.__dlr


    def __preorder_traveral(self, root):

        self.__dlr.append(root.data)

        if root.left != None:
            self.__preorder_traveral(root.left)
        if root.right != None:
            self.__preorder_traveral(root.right)


    @property
    def infix(self):
        """
            In-Order Traversal: 
                L:left-child => D:root => R:right-chid
        """
        self.__inorder_traversal(self.root)

        return self.__ldr


    def __inorder_traversal(self, root):
        if root.left != None:
            self.__inorder_traversal(root.left)

        self.__ldr.append(root.data)

        if root.right != None:
            self.__inorder_traversal(root.right)

        return self.__ldr


    @property
    def postfix(self):
        """
            Post-Order Traversal: 
                L:left-child => R:right-chid => D:root
        """
        self.__postorder_traversal(self.root)

        return self.__lrd


    def __postorder_traversal(self, root):
        if root.left != None:
            self.__postorder_traversal(root.left)

        if root.right != None:
            self.__postorder_traversal(root.right)

        self.__lrd.append(root.data)


    @property
    def layers(self):
        for i in range(1, self.height + 1):
            self.__layerorder_traversal(self.root, i)

        return self.__layer


    def __layerorder_traversal(self, root, level):

        if root is None:
            return

        if level == 1:
            self.__layer.append(root)

        else:
            self.__layerorder_traversal(root.left, level-1)
            self.__layerorder_traversal(root.right, level-1)


    @property
    def height(self):
        return self.__height(self.root)    


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