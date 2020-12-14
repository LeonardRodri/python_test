#!/usr/local/bin/python3
from math import pi


def circulo(raio):
    circuferencia = pi * raio ** 2
    print('A circuferencia do circulo: {:.2f}'.format(circuferencia))


if __name__ == '__main__':
    raio = float(input('Entre com o valor do raio, para obter a circuferencia do circulo.: '))
    circulo(raio)
    print('Nome do modulo', __name__)
