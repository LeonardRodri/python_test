def get_tipo_dia(opc):
    dia = {
        1: deucerto(opc),
        2: deucerto2(opc)
    }

def deucerto(opc):
    print(f'Deu certo {opc}')

def deucerto2(opc):
    print(f'Deu certo2 {opc}')


if __name__ == '__main__':
    opc = int((input('Digita uma opção')))
    get_tipo_dia(opc)
