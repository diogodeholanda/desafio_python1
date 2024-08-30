menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! O limite de saques foi excedido.")
            break

        if valor > saldo:
            print("Operação falou! Saldo insuficiente.")

        elif valor > limite:
            print("Operação falou! Limite excedido.")

        elif valor > 0 and numero_saques < LIMITE_SAQUES:
            valor = float(input("Informe o valor do saque: "))
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(numero_saques)

        elif valor < 0:
            print("Operação falhou! O valor informado é inválido.")

        #excedeu_saldo = valor > saldo

        #excedeu_limite = valor > limite

        #excedeu_saques = numero_saques >= LIMITE_SAQUES

       # if excedeu_saldo:
       #     print("Operação falhou! Você não tem saldo suficiente.")

        #elif excedeu_limite:
        #    print("Operação falhou! O valor do saque excede o limite.")

        #elif excedeu_saques:
        #    print("Operação falhou! Número máximo de saques excedido.")

        #elif valor > 0:
        #    saldo -= valor
        #    extrato += f"Saque: R$ {valor:.2f}\n"
        #    numero_saques += 1

        else:# mantive para o caso do usuário informar uma letra ou caratere diferente
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"\nNúmero de saques: {numero_saques}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")