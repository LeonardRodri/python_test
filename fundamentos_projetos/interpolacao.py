from string import Template

nome, idade = 'Ana', 30.55552

print('Nome: %s Idade %.2f' % (nome, idade))
print('Nome: {0} Idade: {1}'.format(nome, idade))
print(f'Nome: {nome} Idade: {idade}')