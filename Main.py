from Interpreter import *

def main():

	import sys
	text = open(sys.argv[1],'r').read()

	lexer = Lexer(text)
	parser = Parser(lexer)

	tree = parser.parse()
	symtab_builder = SymbolTableBuilder()
	symtab_builder.visit(tree)

	print('')
	print('Symtab contents:')
	print(symtab_builder.symtab)

	interpreter = Interpreter(tree)
	result = interpreter.interpret()

	print('')
	print('Runtime GLOBAL_MEM contents:')

	for k,v in sorted(interpreter.GLOBAL_MEM.items()):
		print('%s = %s' % (k,v))

if __name__ == '__main__':
	main()