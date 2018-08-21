from Token import *

class Lexer(object):

	def __init__(self,text):

		self.text = text
		self.pos = 0
		self.current_char = self.text[self.pos]

	def error(self):

		raise Exception('Invalid char')

	def advance(self):

		self.pos+=1
		if self.pos>len(self.text)-1:
			self.current_char = None
		else:
			self.current_char = self.text[self.pos]

	def peek(self):

		peek_pos = self.pos+1
		if peek_pos > len(self.text)-1:
			return None
		else:
			return self.text[peek_pos]

	def skip_whitespace(self):

		while self.current_char is not None and self.current_char.isspace():
			self.advance()

	def skip_comment(self):

		while self.current_char != '}':
			self.advance()
		self.advance()

	def number(self):

		result = ''
		while self.current_char is not None and self.current_char.isdigit():
			result+=self.current_char
			self.advance()

		if self.current_char == '.':
			result+=self.current_char
			self.advance()

			while self.current_char is not None and self.current_char.isdigit():
				result+=self.current_char
				self.advance()

			token = Token('REAL_CONST',float(result))
		else:
			token = Token('INT_CONST',int(result))

		return token

	def _id(self):

		result = ''
		while self.current_char is not None and self.current_char.isalnum():
			result+=self.current_char
			self.advance()

		token = RESERVED_KEYWORDS.get(result,Token(ID,result))
		return token

	def get_next_token(self):

		while self.current_char is not None:

			if self.current_char.isspace():
				self.skip_whitespace()
				continue

			if self.current_char == '{':
				self.advance()
				self.skip_comment()
				continue

			if self.current_char.isalpha():
				return self._id()

			if self.current_char.isdigit():
				return self.number()

			if self.current_char == ':' and self.peek() == '=':
				self.advance()
				self.advance()
				return Token(ASSIGN,':=')

			if self.current_char == ':':
				self.advance()
				return Token(COLON,':')

			if self.current_char == ';':
				self.advance()
				return Token(SEMI,';')

			if self.current_char == ',':
				self.advance()
				return Token(COMMA,',')

			if self.current_char == '.':
				self.advance()
				return Token(DOT,'.')

			if self.current_char == '+':
				self.advance()
				return Token(PLUS,'+')

			if self.current_char == '-':
				self.advance()
				return Token(MINUS,'-')

			if self.current_char == '*':
				self.advance()
				return Token(STAR,'*')

			if self.current_char == '/':
				self.advance()
				return Token(FLOAT_DIV,'/')
			
			if self.current_char == '(':
				self.advance()
				return Token(LPAREN,'(')

			if self.current_char == ')':
				self.advance()
				return Token(RPAREN,')')

			self.error()
		return Token(EOF,None)