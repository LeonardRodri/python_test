#!/usr/local/bin/python3
from math import pi

print(dir())

raio = float(input('Entre com o valor do raio, para obter a circuferencia do circulo.: '))

circuferencia = pi * raio ** 2

print('A circuferencia do circulo: {:.2f}'.format(circuferencia))
