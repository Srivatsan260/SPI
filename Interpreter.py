from Symtab import *

class Interpreter(NodeVisitor):

	def __init__(self,tree):

		self.tree = tree
		self.GLOBAL_MEM = OrderedDict()

	def visit_Num(self,node):

		return node.value

	def visit_UnaryOp(self,node):

		op = node.op.type

		if op == PLUS:
			return +self.visit(node.expr)
		elif op == MINUS:
			return -self.visit(node.expr)

	def visit_BinOp(self,node):

		op = node.op.type

		if op == PLUS:
			return self.visit(node.left)+self.visit(node.right)
		elif op == MINUS:
			return self.visit(node.left)-self.visit(node.right)
		elif op == STAR:
			return self.visit(node.left)*self.visit(node.right)
		elif op == INT_DIV:
			return self.visit(node.left)//self.visit(node.right)
		elif op == FLOAT_DIV:
			return float(self.visit(node.left))/float(self.visit(node.right))

	def visit_NoOp(self,node):
		pass

	def visit_Compound(self,node):

		for child in node.children:
			self.visit(child)

	def visit_Assign(self,node):

		var_name = node.left.value
		self.GLOBAL_MEM[var_name] = self.visit(node.right)

	def visit_Var(self,node):

		var_name = node.value
		val = self.GLOBAL_MEM.get(var_name)
		return val

	def visit_Program(self,node):

		self.visit(node.block)

	def visit_Block(self,node):

		for declaration in node.declarations:
			self.visit(declaration)
		self.visit(node.compound_statement)

	def visit_VarDecl(self,node):
		pass

	def visit_Type(self,node):
		pass

	def interpret(self):

		tree = self.tree 
		if tree is None:
			return ''
		return self.visit(tree)