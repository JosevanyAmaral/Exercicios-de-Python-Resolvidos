frase = str(input('Digite uma frase:')).strip().lower()
print('A letra "A" aparece {} vezes\nA primeira letra "A" apareceu na posição {}'.format(frase.count('a'), frase.find('a')+1))
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('a')+1))
