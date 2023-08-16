menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[l] Logout

=> """

saldo = 0
limite_saque = 500
extrato = ""
saques_realizados = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d" :
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo_excedido = valor > saldo
        valor_saque_excedido = valor > limite_saque
        limite_saque_excedido = saques_realizados >= LIMITE_SAQUES
    
        if saldo_excedido:
            print("Saque não realizado! Você não tem saldo suficiente.")
        elif valor_saque_excedido:
            print("Saque não realizado! O valor do saque excede o limite disponível.")
        elif limite_saque_excedido:
            print("Saque não realizado! O limite máximo de tentativas foi alcançado.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques_realizados += 1
        else:
            print("Saque não realizado! O valor informado é inválido.")
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
    elif opcao == "l":
        break
    else:
        print("Operação inválida, por favor selecione uma das opções a seguir:")