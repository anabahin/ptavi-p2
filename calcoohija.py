#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class calculadorahija(calcoo.Calculador):

    def multiply(self, n1, n2):
        return (n1 * n2)

    def division(self, n1, n2):
        try:
            return(n1/n2)
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed.")
if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
        calculadora = calculadorahija()

    except ValueError:
        sys.exit("Error not numerical parameters")

    if sys.argv[2] == "suma":
        resultado = calculadora.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        resultado = calculadora.minus(operando1, operando2)
    elif sys.argv[2] == "multiplicar":
        resultado = calculadora.multiply(operando1, operando2)
    elif sys.argv[2] == "division":
            resultado = calculadora.division(operando1, operando2)
    else:
        sys.exit("Error:solo se puede sumar, restar, multiplicar y dividir")

    print(resultado)
