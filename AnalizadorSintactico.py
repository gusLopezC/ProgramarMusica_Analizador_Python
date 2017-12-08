import ply.yacc as yacc
import os
import codecs
import re
from AnalizadorLexico import tokens
from sys import stdin
from AnalizadorSemantico import *

precendecia={
	('rigth','REPRODUCIR','SILENCIO','NOTA','INCREMENTA','DURACION','MUESTRA','CONST','VAR','TEXTO','INICIO','FIN'),
	('rigth','IDENT'),
	('rigth','ASIGNAR'),
	('rigth','IDENT','NUMERO'),
	('left','PARIZQ','PARDER','CORIZQ','CORDER'),
}

def p_program(p):
	'''program : block'''
	print ("program")
	p[0] = program(p[1],"program")

def p_block(p):
	'''block : constDecl varDecl procDecl statement'''
	p[0] = block(p[1],p[2],p[3],p[4],"block")
	print ("block")

def p_constDecl(p):
 	'''constDecl : INICIO constAssignmentList PUNTOCOMA'''
 	p[0] = constDecl(p[2],"constDecl")
 	print("constDecl")

def p_constDeclEmpty(p):
	'''constDecl : empty'''
	p[0] = Null()
	print ("nulo")
	
def p_constAssignmentList1(p):
	'''constAssignmentList : TEXTO IDENT DOSPUNTOS PARENTESIS IDENT PARENTESIS PUNTO'''
	p[0] = constAssignmentList1(p[1],p[2],p[3],p[4],p[5],p[6],p[7],"constAssignmentList1")
	print ("constAssignmentList 1")

def p_constAssignmentList2(p):
	'''constAssignmentList : constAssignmentList IMPORTA CORIZQ IDENT CORDER PUNTO'''
	p[0] = constAssignmentList2(p[1],p[2],p[3],p[4],p[5],p[6],"constAssignmentList2")
	print ("constAssignmentList 2")

def p_constAssignmentList3(p):
	'''constAssignmentList : constAssignmentList CONST  IDENT ASIGNAR IDENT PUNTO'''
	p[0] = constAssignmentList3(p[1],p[2],p[3],p[4],p[5],p[6],"constAssignmentList3")
	print ("constAssignmentList 3")

def p_constAssignmentList4(p):
	'''constAssignmentList : constAssignmentList VAR IDENT ASIGNAR NUMERO PUNTO '''
	p[0] = constAssignmentList4(p[1],p[2],p[3],p[4],p[5],p[6],"constAssignmentList4")
	print ("constAssignmentList 4")

def p_constAssignmentList5(p):
	'''constAssignmentList : constAssignmentList NOTA IDENT PARIZQ IDENT COMA NUMERO PARDER PUNTO '''
	p[0] = constAssignmentList5(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],"constAssignmentList5")
	print ("<con></con>stAssignmentList 5")

def p_constAssignmentList6(p):
	'''consAssignmentList : constAssignmentList REPRODUCIR  PARIZQ IDENT COMA DURACION PARDER PUNTO '''
	p[0] = constAssignmentList6(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],"constAssignmentList6")
	print ("constAssignmentList 6")

def p_constAssignmentList62(p):
	'''constAssignmentList : constAssignmentList REPRODUCIR  PARIZQ IDENT COMA NUMERO PARDER PUNTO '''
	p[0] = constAssignmentList62(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],"constAssignmentList62")
	print ("constAssignmentList 62")

def p_constAssignmentList63(p):
	'''constAssignmentList : constAssignmentList REPRODUCIR  PARIZQ IDENT COMA NUMERO POR IDENT PARDER PUNTO '''
	p[0] = constAssignmentList63(p[1],p[2],p[3],p[4],[5],p[6],p[7],p[8],p[9],p[10],"constAssignmentList63")
	print ("constAssignmentList 63")

def p_constAssignmentList7(p):
	'''constAssignmentList : constAssignmentList SILENCIO PARIZQ NUMERO PARDER PUNTO'''
	p[0] = constAssignmentList7(p[1],p[2],p[3],p[4],p[5],p[6],"constAssignmentList7")
	print ("constAssignmentList 7")

def p_constAssignmentList8(p):
	'''constAssignmentList : constAssignmentList INCREMENTA PARIZQ IDENT AUMENT  NUMERO PARDER PUNTO  '''
	p[0] = constAssignmentList8(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],"constAssignmentList8")
	print ("constAssignmentList 8")

def p_constAssignmentList9(p):
	'''constAssignmentList : constAssignmentList MUESTRA  PARIZQ TEXTO PARDER PUNTO '''
	p[0] = constAssignmentList9(p[1],p[2],p[3],p[4],p[5],p[6],"constAssignmentList8")
	print ("constAssignmentList 9")

def p_constAssignmentList10(p):
	'''constAssignmentList : constAssignmentList DURACION ASIGNAR NUMERO PUNTO '''
	p[0] = constAssignmentList10(p[1],p[2],p[3],p[4],p[5],"constAssignmentList8")
	print ("constAssignmentList 10")

def p_constAssignmentList11(p):
	'''constAssignmentList : constAssignmentList FIN PUNTOCOMA'''
	p[0] = constAssignmentList10(p[1],p[2],p[3],"constAssignmentList8")
	print ("constAssignmentList 11")

#----------end declaracion constantes----------------
def p_varDeclEmpty(p):
	'''varDecl : empty'''
	p[0] = Null()
	#print ("nulo o no usado")
#----------end declaracion variables------------------
def p_procDeclEmpty(p):
	'''procDecl : empty'''
	p[0] = Null()
	#print ("nulo o no usado")
#----------end declaracion procedencia----------------
def p_statementEmpty(p):
	'''statement : empty'''
	p[0] = Null()
	#print ("nulo o se usa ")

#-------------------------------------------------------
def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print(p)
	#print("error en la linea "+str(p.lineno))

def traducir(result):
	graphFile =  open('graphiztrhee.vz','w')
	graphFile.write(result.traducir())
	graphFile.close
	print("\t\tEl programa traducido se guardo en \"graphviztrhee.vz\"")


archivo = '/home/gus/Projects/ComposicionMusica/test/prueba1.pl0' 
fp = codecs.open(archivo,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)


result.imprimir(" ")
#print(result.traducir())
traducir(result)


print(result)