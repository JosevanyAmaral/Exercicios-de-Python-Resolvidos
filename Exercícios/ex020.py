from random import shuffle
aluno1 = (input('Digite o nome do primeiro aluno:'))
aluno2 = (input('Digite o nome do segundoo aluno:'))
aluno3 = (input('Digite o nome do terceiro aluno:'))
aluno4 = (input('Digite o nome do quarto aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será: \n{}'.format(lista))
