pessoa = {'nome': 'Leonardo', 'idade': 25, 'cursos': ['Ingles', 'Portugues']}
print(pessoa)

print(pessoa['nome'])

pessoa2 = {'nome': 'Leonardo Rodrigues', 'idade': 45, 'cursos': ['React','Python']}

pessoa2['idade'] = 44
pessoa2['cursos'].append('Angular')
pessoa2.update({'idade': 40, 'Sexo': 'M'})

print(pessoa2)