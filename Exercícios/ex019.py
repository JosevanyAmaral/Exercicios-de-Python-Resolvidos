from random import choice
aluno1 = (input('Digite o nome do primeiro aluno:'))
aluno2 = (input('Digite o nome do segundoo aluno:'))
aluno3 = (input('Digite o nome do terceiro aluno:'))
aluno4 = (input('Digite o nome do quarto aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4]
print('{}, você foi sorteado(a) para apagar o quadro'.format(choice(lista)))
