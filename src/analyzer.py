import exprParser as parser


def Compute(lrd: list):
	result = []
	for e in lrd:
		if e not in parser.Tokens:
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

