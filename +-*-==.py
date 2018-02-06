from time import sleep
n1 = int(input("Digite um primeiro valor: "))
n2 = int(input("Digite um segundo valor: "))
opção = 0
while opção != 5:
    print(''' Opções:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')
    opção = int(input("Escolha uma opção: "))
    print("-=" * 20)
    if opção == 1:
        soma = n1+n2
        print("A soma de {} e {} é {}".format(n1,n2,soma))

    elif opção == 2:
        multi= n1*n2
        print("A multiplicação de {} e {} é {}".format(n1,n2,multi))

    elif opção == 3:
            if n1>n2:
                print("O maior é {}".format(n1))
            else: print("O maior é {}".format(n2))

    elif opção == 4:
        n1 = int(input("Digite um primeiro valor: "))
        n2 = int(input("Digite um segundo valor: "))


    elif opção != opção:
        print("Opção não encontrada tente novamente.")
    sleep(0.5)


print("Saindo...")
sleep(2)

