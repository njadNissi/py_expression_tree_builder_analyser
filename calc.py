from binary_node import BNode
from binary_tree import BTree
import conversor as conv
from virtual_btree import visualize_binary_tree as vtree


def calc(lrd: list):
	result = []
	for e in lrd:
		if e not in conv.Symbols:
			result.append(float(e))
		else:
			print('当前堆：', result[::-1])
			print('operate with -> ', e)
			op = e
			num2 = result.pop()
			num1 = result.pop()
			if op == '+':
				result.append(num1 + num2)
			elif op == '-':
				result.append(num1 - num2)
			elif op == '*':
				result.append(num1 * num2)
			elif op == '/':
				result.append(num1 / num2)
			elif op == '^':
				result.append(num1 ** num2)

	return result.pop()


def ex_manual_build_tree():
	a = BNode(data=1)
	b = BNode(data=3)
	c = BNode(data=2)
	d = BNode(data=5)
	f = BNode(data='+', lchild=a, rchild=b)
	g = BNode(data='*', lchild=c, rchild=d)
	e = BNode(data='-', lchild=f, rchild=g)

	tree = BTree(e)
	nodes = [n.data for n in tree.Layer()]
	print('层序', nodes)
	nodes = tree.DLR()

	print('前序', nodes)

	nodes = tree.LDR()
	print('中序', nodes)

	nodes = tree.LRD()
	print('后序', nodes)

	print('Result:', calc(nodes))
	print('HEIGHT:', tree.HEIGHT)

	vtree(root=e)


def ex_conversion():
	# infix = '(-12 + 34) * (56 / 7)'
	# infix = '3+6-5*4-3+8*(7-3)/2+1-9/3-2'
	infix = input('Enter infix expression: ')
	postfix = conv.infixToPostfix(infix)
	print('postfix notation: ', postfix)
	print('Result:', calc(postfix))


def ex_auto_build_tree():
	infix = '(-12+34)*(56/7)'
	# infix = '3+6-5*4-3+8*(7-3)/2+1-9/3-2'
	# infix = input('Enter infix expression: ')
	# postfix = LRD.infixToPostfix(infix)
	# tree_root = BTree.from_postfix(postfix)
	print('EXPRESSION: ' + infix)
	tree_root = BTree.from_infix(conv.parse_infix(infix))
	vtree(tree_root)


if __name__=="__main__":

	ex_auto_build_tree()