# -*- coding: utf-8 -*-
from Pila import Pila

class postfija:
        
    arbolbase = Pila()
    entrada = input()
    lista = entrada.split(" ")
    #print(lista)
    for element in lista:
        if (element == '+' or element == '-' or element == '*'
            or element == '/'):
            puntder=float(arbolbase.desapilar())
            puntizq=float(arbolbase.desapilar())
            if element=='+':
                arbolbase.apilar(puntizq + puntder)
            if element=='-':
                arbolbase.apilar(puntizq - puntder)
            if element=='*':
                arbolbase.apilar(puntizq * puntder)
            if element=='/':
                arbolbase.apilar(puntizq / puntder)  
        else:
            #print (element)
            arbolbase.apilar(element)
            
    print (arbolbase.desapilar())
