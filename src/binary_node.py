class BNode:

	def __init__(self, data, lchild=None, rchild=None):
		self.data = data
		self.left = lchild
		self.right = rchild		

	def set_children(self, lchild=None, rchild=None):
		"""
			The order of calling args: first right-child then left-child, is chosen on purpose,
			so that during calls like : node = BNode(stack.pop(), stack.pop()) is matched
			instead of: 
                right = tree.pop()  
                left = tree.pop()              
				node = BNode(left, right)

		"""
		self.left = lchild
		self.right = rchild		
