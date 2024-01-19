from binary_node import BNode
from binary_tree import BTree
from analyzer import Compute
from virtual_btree import visualize_binary_tree as vtree
from exprParser import infixToPostfix, parse_infix

def ex_manual_build_tree():
	a = BNode(data=1)
	b = BNode(data=3)
	c = BNode(data=2)
	d = BNode(data=5)
	f = BNode(data='+', lchild=a, rchild=b)
	g = BNode(data='*', lchild=c, rchild=d)
	e = BNode(data='-', lchild=f, rchild=g)

	tree = BTree(e)

	print('层序', tree.layers)
	
	print('前序', tree.prefix)

	print('中序', tree.infix)

	print('后序', tree.postfix)

	print('Result:', Compute(tree.postfix))
	print('HEIGHT:', tree.height)

	vtree(root=e)


def ex_conversion():
	# infix = '(-12 + 34) * (56 / 7)'
	# infix = '3+ 6-5*4-3+8 *(7- 3)/2 +1-9/3-2'
	infix = input('Enter infix expression: ')
	postfix = infixToPostfix(infix)
	print('postfix notation: ', postfix)
	print('Result:', Compute(postfix))


def ex_auto_build_tree():
	# infix = '(-12+34)*((6^2)/18)'
	infix = '1+2-3*4-5+6*(7-8)/1+10-24/12-5'
	# infix = input('Enter infix expression: ')
	# postfix = LRD.infixToPostfix(infix)
	# tree_root = BTree.from_postfix(postfix)
	print('EXPRESSION: ' + infix)
	tree = BTree.from_infix(parse_infix(infix))
	postfix = tree.postfix
	print('postfix notation: ', postfix) 
	print('Result:', Compute(postfix))
	vtree(tree.root)




if __name__=="__main__":

	ex_auto_build_tree()
	# ex_manual_build_tree()