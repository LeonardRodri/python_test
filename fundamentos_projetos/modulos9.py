#!/usr/local/bin/python3
from math import pi


def circulo(raio):
    return pi * raio ** 2


if __name__ == '__main__':
    raio = float(input('Entre com o valor do raio, para obter a circuferencia do circulo.: '))
    area = circulo(raio)
    print('Area do circulo e: ', area)
