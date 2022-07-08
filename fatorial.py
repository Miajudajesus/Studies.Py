numero = int(input('Insira um número: ') )

resultado = 1
contador = 1

while contador <= numero:
    resultado *= contador
    contador += 1

print('\nO fatorial deste número é', resultado)
