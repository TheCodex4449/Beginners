# -*- coding: utf-8 -*-
"""
Created on Mon May 12 14:38:00 2025

@author: Jonathan Belmont
"""

def Conversor_Faren (x):
    return (x * 1.8) + 32 

def Conversor_Celsius (y):
    return (y - 32) * 5/9

y = int(input("Insira a temperatura em Farenheit: "))
x = int(input("Insira a temperatura em Celsius: "))
celsius = Conversor_Celsius(y)
farenheit = Conversor_Faren(x)
print (f"A temperatura em Farenheit é {farenheit}")
print (f"A temperatura em Celsius é {celsius:.1f}")