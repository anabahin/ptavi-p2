#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

try:
    fichero = sys.argv[1]
except:
    sys.exit("fichero not found")

abrir = open('fichero.csv', 'r')
    
if __name__ == "__main__":
    with open(abrir) as file:
        linea = csv.reader(file)
        calculadora = calcoohija.calculadorahija()
        for linea in lineas:
            linea_cortada = linea.split(',')
            #print(linea_cortada, len(linea_cortada))
            operando = linea_cortada[0]
            numero1 = int(linea_cortada[1])
            #print(numero1)
            numeros = linea_cortada[2:]
            #print(numeros)
        
        
            if operando == "suma":
                num_actual = numero1
                for num in numeros:
                    print(num)
                    num_actual = calculadora.plus(num_actual,int(num))
                print(num_actual)
            
            elif operando == "resta":
                num_actual=numero1
                for num in numeros:
                    print(num)
                    num_actual = calculadora.minus(num_actual,int(num))
                print(num_actual)
            
            elif operando == "multiplicacion":
                num_actual=numero1
                for num in numeros:
                    print(num)
                    num_actual = calculadora.multiply(num_actual,int(num))
                print(num_actual)
        
            elif operando == "division":
                num_actual=numero1
                print(num_actual)
                for num in numeros:
                    print(num)
                    num_actual = calculadora.division(num_actual,float(num))
                print(num_actual)