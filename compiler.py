# -*- coding: utf-8 -*-
from pila import Pila

operadores=['*','+','-','/','=']

#Pruebas de validacion de carácteres
def esVariable (caracter):
    if caracter.isupper():
       # print(caracter)
        if caracter.isalpha():
            #print("bien")
            return True
    return False

def esNumero (caracter):
    try:
        caracter = float(caracter)
        return True
    except ValueError:
        return False
    
def esOperador(caracter):
    for x in operadores:
        if caracter==x:
            return True
    return False

#Inicio del proceso
class Elemento:
    pilaC= Pila()
    dic=[]
    listaC=[y.split(' ') for y in [x.strip('\n') for x in open("caracteres.txt", 'r').readlines()]]
    i=0
    for x in listaC:
        for element in x:
            if esVariable(element)==True or esNumero(element)==True or esOperador(element)==True:
                #print ("entro")
                for s in dic:
                        for y in s:
                            if y==element:
                                element=s[1]
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
                        print m , " = ", n
                        
                        dic.append([m,n])
                    if(element != '='):
                        pilaC.apilar(element)

            else:
                print "El caracter (", element , ") No se reconoce" 
                break
        else:
            continue
        break
        

                
    #print (dic)
