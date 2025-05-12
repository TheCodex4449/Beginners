# -*- coding: utf-8 -*-
"""
Created on Mon May 12 11:55:57 2025

@author: Jonathan_Belmont
"""
a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))

print("(1) = Soma")
print("(2) = Subtração")
print("(3) = Multiplicação")
print("(4) = Divisão")

opcao_escolhida = input("Escolha uma opção digite: ")

def Calcule (opcao_escolhida):
    if opcao_escolhida == "1":
        return a + b
    if opcao_escolhida == "2":
        return a - b
    if opcao_escolhida == "3":
        return a * b
    if opcao_escolhida == "4":
        return a / b
        
print (Calcule(opcao_escolhida))