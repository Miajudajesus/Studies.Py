numUsuario1 = int (input('Digite o primeiro número: '))
numUsuario2 = int (input('Digite o segundo número: '))
numUsuario3 = int (input('Digite o terceiro número: '))

if numUsuario1 > numUsuario2 and numUsuario1 > numUsuario3:
    print('\nO primeiro número é o maior!')

elif numUsuario1 < numUsuario2 and numUsuario2 > numUsuario3:
    print('\nO segundo número é o maior!')

elif numUsuario3 > numUsuario2 and numUsuario3 > numUsuario1:
    print('\nO terceiro número é o maior!')

elif numUsuario1 == numUsuario2 and numUsuario2 == numUsuario3:
    print('\nOs números são iguais!')
