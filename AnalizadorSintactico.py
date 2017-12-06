import ply.yacc as yacc
import os
import codecs
import re
from AnalizadorLexico import tokens
from sys import stdin

precendecia={
	('rigth','IDENT'),
	('rigth','ASIGNAR'),
	('rigth','IDENT'),
	('left','MENORQUE','MENORIGUAL','MAYORQUE','MAYORIGUAL','IGUAL'),
	('left','PARIZQ','PARDER','CORIZQ','CORDER','LLAIZQ','LLADER'),
}

def p_program(p):
	'''program : block'''
	print("program")
	#p[0] = program(p[1],"program")
def p_block(p):
	'''block : constDecl varDecl procDecl statement'''
	print("block")

def p_constDecl(p):
	'''constDecl : const constAssignmentList'''
	#p[0] = constDecl(p[2])
	print("constDecl")

def p_constDeclEmpty(p):
	'''constDecl : empty '''
	#p[0] = null()
	print("nulo")

def p_empty(p):
	'''emptry :'''
	pass

def p_error(p):
	print("Error de sintaxis"+p)
	print("error en la linea "+str(p.lineno))

archivo = '/home/gus/Projects/ComposicionMusica/test/prueba1.pl0' 
fp = codecs.open(archivo,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)
#print("---------------------------- Analizador SIntactico ----------------------------")

print(result)