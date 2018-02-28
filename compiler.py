# -*- coding: utf-8 -*-
from pila import Pila
class Elemento:
    pilaC= Pila()
    dic=[]
    listaC=[y.split(' ') for y in [x.strip('\n') for x in open("caracteres.txt", 'r').readlines()]]
    i=0
    for x in listaC:
        for element in x:
            if (element == '+' or element == '-' or element == '*'
                or element == '/'):
                puntder=float(pilaC.desapilar())
                puntizq=float(pilaC.desapilar())
                if element=='+':
                    pilaC.apilar(puntizq + puntder)
                if element=='-':
                    pilaC.apilar(puntizq - puntder)
                if element=='*':
                    pilaC.apilar(puntizq * puntder)
                if element=='/':
                    pilaC.apilar(puntizq / puntder)  
            else:
                #print (element)
                if(element == '='):
                    m=pilaC.desapilar()
                    n=pilaC.desapilar()
                    print m
                    print n
                    dic.append(m)
                    dic.append(n)
                if(element != '='):
                    pilaC.apilar(element)
                
        
    print (dic)
