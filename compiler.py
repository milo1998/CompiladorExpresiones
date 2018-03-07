# -*- coding: utf-8 -*-
from pila import Pila

operadores=['*','+','-','/','=']

#Pruebas de validacion de carácteres
def esVariable (caracter):
    if caracter.isupper():
        if caracter.isalpha():
            return True
    return False

def esNumero (caracter):
    try:
        caracter = int(caracter)
        return True
    except ValueError:
        return False
    
def esOperador(caracter):
    for x in operadores:
        if caracter == x:
            return True
    return False

#Inicio del proceso
class Elemento:
    pilaC = Pila()
    dic = []
    listaC = [y.split(' ') for y in [x.strip('\n') for x in open("caracteres.txt", 'r').readlines()]]
    f = False
    for x in listaC:
        for element in x:
            if esVariable(element) == True or esNumero(element) == True or esOperador(element) == True:
                for s in dic:
                        for y in s:
                            if y == element:
                                element = s[1]
                if (element == '+' or element == '-' or element == '*' or element == '/'):
                    if pilaC.es_vacia()==False:
                        puntderecho=(pilaC.desapilar())
                    else:
                        print "Error de sintaxis"
                        f=True
                        break
                    if pilaC.es_vacia()==False:
                        puntizquierdo=(pilaC.desapilar())
                    else:
                        print "Error de sintaxis"
                        f=True
                        break
                    
                    if (esNumero(puntderecho)==True and esNumero(puntizquierdo)==True):
                        puntder=int(puntderecho)
                        puntizq=int(puntizquierdo)
                    else:
                        print ("Variable No definida")
                        f=True
                        break
                    if element=='+':
                        pilaC.apilar(puntizq + puntder)
                    if element=='-':
                        pilaC.apilar(puntizq - puntder)
                    if element=='*':
                        pilaC.apilar(puntizq * puntder)
                    if element=='/':
                        if(puntder == 0):
                            print("Error de compilacion: Division por 0")
                            f=True
                            break
                        else:
                            pilaC.apilar(puntizq / puntder)  
                else:                   
                    if(element == '='):
                        if pilaC.es_vacia()==False:
                            m = pilaC.desapilar()
                        else:
                            print "Error de sintaxis "
                            f=True
                            break
                        if pilaC.es_vacia()==False:
                            n = pilaC.desapilar()
                        else:
                            print "Error de sintaxis "
                            f=True
                            break
                        if(pilaC.es_vacia() == False):
                            print "Error de sintaxis "
                            f=True
                            break
                        
                        dic.append([m,n])
                        
                    if(element != '='):
                        pilaC.apilar(element)

            else:
                print "El caracter (", element , ") No se reconoce"
                f = True
                break
           
        else:
            if(pilaC.es_vacia() == False):
                print "Error de sintaxis"
                f=True
                break
            continue
        break

    
    if f == False:
        for x, y in dic:
            print x ,"=", y
