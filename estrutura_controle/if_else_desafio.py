# CONCEITO    NOTAS
# A            DE 10,0 Á 9,1
# A-           DE 9,0 Á 8,1
# B            DE 8,0,0 Á 7,1
# B-           DE 7,0 Á 6,1
# C            DE 6,0 Á 5,1
# C-           DE 5,0 Á 4,1
# D            DE 4 Á 3,1
# D-           DE 3 Á 2,1
# A            DE 2,0 Á 1,1
# E            DE 1,0 Á 1,0

# Para notas maiores que 10 e menores que 0 sera impresso 'Nota invalida'

def convert_nota(nota):
    nota = float(nota)
    if nota > 10:
        print("Nota Invalida")
        pass
    if nota >= 9.1 and nota <= 10:
        print("A sua nota e A")
        pass
    elif nota <= 9 and nota >= 8.1:
        print("A sua nota e A-")
        pass
    elif nota <= 8 and nota >= 7.1:
        print("A sua nota e B")
        pass
    elif nota <= 7 and nota >= 6.1:
        print("A sua nota e C")
        pass
    elif nota <= 6 and nota >= 5.1:
        print("A sua nota e D")
        pass
    elif nota <= 5 and nota >= 4.1:
        print("A sua nota e D-")
        pass
    elif nota <= 3 and nota >= 2.1:
        print("A sua nota e E")
        pass
    elif nota <= 2 and nota >= 1.1:
        print("A sua nota e -E")
        pass
    elif nota <= 1 and nota >= 0.0:
        print("A sua nota e -E")
        pass


if __name__ == '__main__':
    nota = float(input("Digite a sua nota: "))
    convert_nota(nota)
