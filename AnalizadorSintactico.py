import ply.yacc as yacc
import os
import codecs
import re
from AnalizadorLexico import tokens
from sys import stdin

precendecia={
	('rigth','REPRODUCIR','SILENCIO','NOTA','INCREMENTA','DURACION','MUESTRA',
    'CONST','VAR','TEXTO','INICIO','FIN'),
	('rigth','IDENT'),
	('rigth','ASIGNAR'),
	('rigth','IDENT'),
	('left','PARIZQ','PARDER','CORIZQ','CORDER','LLAIZQ','LLADER'),
}

def p_program(p):
	'''program : block'''
	print ("program")
	#p[0] = program(p[1],"program")

def p_block(p):
	'''block : constDecl varDecl procDecl statement'''
	#p[0] = block(p[1],p[2],p[3],p[4],"block")
	print ("block")

def p_constDecl(p):
 	'''constDecl : INICIO constAssignmentList PUNTOCOMA'''
 	print("constDecl")

 	#p[0] = constDecl(p[2],"constDecl")
	

def p_constDeclEmpty(p):
	'''constDecl : empty'''
	print ("nulo")
	#p[0] = Null()
		

def p_constAssignmentList1(p):
	'''constAssignmentList : TEXTO IDENT DOSPUNTOS PARENTESIS IDENT PARENTESIS PUNTO'''
	#p[0] = constAssignmentList1(Texto(p[1]),Id(p[2]),Dospuntos(p[3]),Parentesis(p[4]),Id(p[5]),Parentesis(p[6]),Punto(p[7]),"constAssignmentList1")
	print ("constAssignmentList 1")

def p_constAssignmentList2(p):
	'''constAssignmentList : constAssignmentList IMPORTA CORIZQ IDENT CORDER PUNTO'''
	#p[0] = constAssignmentList2(Importa(p[1]),CorIzq(p[2]),Id(p[3]),CorDer(p[4]),Punto(p[5]),"constAssignmentList2")
	print ("constAssignmentList 2")

def p_constAssignmentList3(p):
	'''constAssignmentList : constAssignmentList CONST  IDENT ASIGNAR IDENT PUNTO'''
	#p[0] = constAssignmentList3(Importa(p[1]),CorIzq(p[2]),Id(p[3]),CorDer(p[4]),Punto(p[5]),"constAssignmentList2")
	print ("constAssignmentList 3")

def p_constAssignmentList4(p):
	'''constAssignmentList : constAssignmentList VAR IDENT ASIGNAR NUMERO PUNTO '''
	#p[0] = constAssignmentList4(Importa(p[1]),CorIzq(p[2]),Id(p[3]),CorDer(p[4]),Punto(p[5]),"constAssignmentList2")
	print ("constAssignmentList 4")

def p_constAssignmentList5(p):
	'''constAssignmentList : constAssignmentList NOTA IDENT PARIZQ IDENT COMA NUMERO PARDER PUNTO '''
	#p[0] = constAssignmentList5(Importa(p[1]),CorIzq(p[2]),Id(p[3]),CorDer(p[4]),Punto(p[5]),"constAssignmentList2")
	print ("constAssignmentList 5")

def p_constFAssignmentList6(p):
	'''constAssignmentList : constAssignmentList REPRODUCIR  PARIZQ IDENT COMA DURACION PARDER PUNTO '''
	#p[0] = constAssignmentList6(Importa(p[1]),CorIzq(p[2]),Id(p[3]),CorDer(p[4]),Punto(p[5]),"constAssignmentList2")
	print ("constAssignmentList 6")

def p_constFAssignmentList62(p):
	'''constAssignmentList : constAssignmentList REPRODUCIR  PARIZQ IDENT COMA NUMERO PARDER PUNTO '''
	#p[0] = constAssignmentList62(Importa(p[1]),CorIzq(p[2]),Id(p[3]),CorDer(p[4]),Punto(p[5]),"constAssignmentList2")
	print ("constAssignmentList 62")

def p_constFAssignmentList63(p):
	'''constAssignmentList : constAssignmentList REPRODUCIR  PARIZQ IDENT COMA NUMERO POR IDENT PARDER PUNTO '''
	#p[0] = constAssignmentList63(Importa(p[1]),CorIzq(p[2]),Id(p[3]),CorDer(p[4]),Punto(p[5]),"constAssignmentList2")
	print ("constAssignmentList 63")


def p_constAssignmentList7(p):
	'''constAssignmentList : constAssignmentList SILENCIO PARIZQ NUMERO PARDER PUNTO'''
	#p[0] = constAssignmentList7(Importa(p[1]),CorIzq(p[2]),Id(p[3]),CorDer(p[4]),Punto(p[5]),"constAssignmentList2")
	print ("constAssignmentList 7")

def p_constAssignmentList8(p):
	'''constAssignmentList : constAssignmentList INCREMENTA PARIZQ IDENT AUMENT  NUMERO PARDER PUNTO  '''
	#p[0] = constAssignmentList8(Importa(p[1]),CorIzq(p[2]),Id(p[3]),CorDer(p[4]),Punto(p[5]),"constAssignmentList2")
	print ("constAssignmentList 8")


def p_constAssignmentList9(p):
	'''constAssignmentList : constAssignmentList MUESTRA  PARIZQ TEXTO PARDER PUNTO '''
	#p[0] = constAssignmentList9(Importa(p[1]),CorIzq(p[2]),Id(p[3]),CorDer(p[4]),Punto(p[5]),"constAssignmentList2")
	print ("constAssignmentList 9")

def p_constAssignmentList10(p):
	'''constAssignmentList : constAssignmentList DURACION ASIGNAR NUMERO PUNTO '''
	#p[0] = constAssignmentList9(Importa(p[1]),CorIzq(p[2]),Id(p[3]),CorDer(p[4]),Punto(p[5]),"constAssignmentList2")
	print ("constAssignmentList 10")

def p_constAssignmentList11(p):
	'''constAssignmentList : constAssignmentList FIN PUNTOCOMA'''
	#p[0] = constAssignmentList10(Importa(p[1]),CorIzq(p[2]),Id(p[3]),CorDer(p[4]),Punto(p[5]),"constAssignmentList2")
	print ("constAssignmentList 11")


#----------end declaracion constantes----------------
def p_varDeclEmpty(p):
	'''varDecl : empty'''
	#p[0] = Null()
	print ("nulo o no usado")
#----------end declaracion variables------------------

def p_procDeclEmpty(p):
	'''procDecl : empty'''
	#p[0] = Null()
	print ("nulo o no usado")
#----------end declaracion procedencia----------------


def p_statementEmpty(p):
	'''statement : empty'''
	#p[0] = Null()
	print ("nulo o se usa ")

#-------------------------------------------------------
def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print(p)
	#print("error en la linea "+str(p.lineno))

archivo = '/home/gus/Projects/ComposicionMusica/test/prueba1.pl0' 
fp = codecs.open(archivo,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)
print(result)