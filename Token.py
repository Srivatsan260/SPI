from collections import OrderedDict

INTEGER 	= 'INTEGER'
REAL		= 'REAL'
INT_CONST   = 'INT_CONST'
REAL_CONST  = 'REAL_CONST'
INT_DIV		= 'INT_DIV'
FLOAT_DIV	= 'FLOAT_DIV'
PROGRAM		= 'PROGRAM'
VAR			= 'VAR'
ASSIGN		= 'ASSIGN'
BEGIN		= 'BEGIN'
END			= 'END'
DOT			= 'DOT'
COLON 		= 'COLON'
SEMI		= 'SEMI'
COMMA		= 'COMMA'
ID 			= 'ID'
LPAREN		= 'LPAREN'
RPAREN		= 'RPAREN'
PLUS		= 'PLUS'
MINUS		= 'MINUS'
STAR		= 'STAR'
EOF			= 'EOF'

class Token(object):

	def __init__(self,type,value):

		self.type = type
		self.value= value

	def __str__(self):

		return 'Token({type},{value})'.format(type=self.type,value=repr(self.value))

	__repr__ = __str__


RESERVED_KEYWORDS = {
	'PROGRAM' : Token('PROGRAM','PROGRAM'),
	'VAR' : Token('VAR','VAR'),
	'BEGIN' : Token('BEGIN','BEGIN'),
	'END' : Token('END','END'),
	'DIV' : Token('INT_DIV','DIV'),
	'INTEGER' : Token('INTEGER','INTEGER'),
	'REAL' : Token('REAL','REAL'),
}