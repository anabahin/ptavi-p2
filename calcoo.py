#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculador():
    
    def plus(self, n1, n2):
        return (n1 + n2)
    def minus(self, n1, n2):
        return (n1 - n2)
    
if __name__ == "__main__":
    
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
        calculadora = Calculador()
        
    except ValueError:
        sys.exit("Error: Non numerical parameters")
        
        
    if sys.argv[2] == "suma":
        resultado = calculadora.plus(operando1, operando2)
    elif sys.argv[2]== "resta":
        resultado = calculadora.minus(operando1, operando2)
    else:
        sys.exit("Error:solo se puede sumar o restar")
        
    print(resultado)
        
    
        