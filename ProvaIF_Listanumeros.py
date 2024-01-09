from functools import reduce

numeros = [1 ,2 , 3, 4, 5, 6, 7, 8, 9, 10]

quad_num = list(map(lambda num: num ** 2, numeros))

pares = list(filter(lambda num: num % 2 == 0, numeros))

soma = reduce(lambda num1, num2: num1 + num2, numeros)

print('\nBem vindo ao Match-FunçõesLambda!')
while True:
    decisao = int(input('\nMarque qual opção deseja:\n \n(1)Quadrado dos números\n \n(2)Números pares da lista\n \n(3)Soma cumulativa da lista\n \n(4)Sair\n\n'))
    match decisao:
        case 1:
            print(f'\nO quadrado dos números da lista {numeros} é respectivamente: \n{quad_num}.\n')

        case 2:
            print(f'\nOs números pares da lista {numeros} é: \n{pares}.\n')

        case 3:
            print(f'\nA soma cumulativa dos números da lista {numeros} é: {soma}.\n')

        case 4:
            print('\nObrigado por utilizar o programa!\n')
            break