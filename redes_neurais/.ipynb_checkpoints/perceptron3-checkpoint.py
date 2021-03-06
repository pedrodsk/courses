# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 20:09:23 2021

@author: Pedro
"""

# =============================================================================
# terceiro programa do curso de redes neurais com python. 
# ajustes de pesos.
# =============================================================================

import numpy as np

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0,0,0,1])
pesos = np.array([0.0,0.0])
pesos
taxaAprendizagem = 0.1

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

# =============================================================================
# Enquanto o erro for diferente de zero
# Para cada registro 
# Calcula a saida 
# =============================================================================
def treinar():
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.array(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j]+= (taxaAprendizagem * entradas[i][j] * erro)
            print('Peso atualizado: ' + str(pesos[j]))
        print('total de erro ' + str(erroTotal))

treinar()