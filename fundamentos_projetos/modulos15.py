#!/usr/local/bin/python3
from math import pi
import sys

ERRO = '\033[91m'
NORMAL = '\033[0m'

def circulo(raio):
    return pi * float(raio) ** 2

def help(script):
    print('E necessario informar o raio do circulo.')
    print(f'Sintaxe: {script} <raio>')



if __name__ == '__main__':
    if len(sys.argv) < 2:
        help(sys.argv[0])
        sys.exit(1)
    elif not sys.argv[1].isnumeric():
        help(sys.argv[0])
        print(ERRO,"A opção nao e numerico", NORMAL)
        sys.exit(2)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Area do circulo e: ', area)
