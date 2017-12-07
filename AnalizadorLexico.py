import ply.lex as lex
import re
import codecs
import os
import sys

reservadas=[ 'REPRODUCIR','IMPORTA','SILENCIO','NOTA','INCREMENTA','DURACION','MUESTRA',
          'CONST','VAR','TEXTO','INICIO','FIN'
          ]


tokens = reservadas + ['IDENT','NUMERO','ASIGNAR',
          'PUNTOCOMA','COMA','PUNTO','DOSPUNTOS','PARENTESIS',
          'AUMENT','POR',
     	'PARIZQ','PARDER', #()
     	'CORIZQ','CORDER', #[]
     	#'LLAIZQ','LLADER' #{}
           ] 

t_ignore = '\t'
t_ASIGNAR = r'=='
     
t_DOSPUNTOS = r':'
t_PUNTO= r'\.'
t_PUNTOCOMA  = r';'
t_COMA  = r','
t_POR = r'\*'
t_AUMENT = r'\+\+'

t_PARENTESIS = r'\"'
t_PARIZQ  = r'\('
t_PARDER  = r'\)'
t_CORIZQ  = r'\['
t_CORDER  = r'\]'
#t_LLAIZQ  = r'\{'
#t_LLADER  = r'\}'


def t_IDENT(t):
     r'[a-zA-Z_][a-zA-Z0-9_]*'
     if t.value.upper() in reservadas:
          t_value = t.value.upper()
          t.type = t.value
     return t

def t_nuevaline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

def t_COMENTARIO(t):
     r'\@.*'
     t.lexer.lineno += t.value.count('\n')
     print("Comentario")

def t_ccode_nonspace(t):
          r'\s'
          pass

def t_NUMERO(t):
     r'\d+'
     t.value= int(t.value)
     return t

def t_error(t):
     print("Caracter invalido no reconocido "+t.value[0])
     t.lexer.skip(1)


archivo = '/home/gus/Projects/ComposicionMusica/test/prueba1.pl0' 
fp = codecs.open(archivo,"r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)
print("------------------------------------ Analizador Lexico -----------------------------------------")
while True:
     tok = analizador.token()
     if not tok : break
     print (tok)


print("-----------------------------------------------------------------------------------------------")