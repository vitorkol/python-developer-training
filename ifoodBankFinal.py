"""
Este código foi baseado nas sugestões e orientações fornecidas pelo Prof. Guilherme  DIO
sendo parte essencial para o desenolvimendo das atividades do curso Formação Python Deve
loper/Python Developer Training.
Autor: [Vitor Campos]
GitHub: [https://github.com/vitorkol]
Repositório Original: [https://github.com/vitorkol/python-developer-training]
Data: [2023-08-19]
"""

# [Aqui vem o restante do seu código]

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato, valor_limite_saque, numero_saques, limite_saques):
    saldo_excedido = valor > saldo
    valor_saque_excedido = valor > valor_limite_saque
    limite_saque_excedido = numero_saques >= limite_saques

    if saldo_excedido:
        print("Saque não realizado! Você não tem saldo suficiente.")
    elif valor_saque_excedido:
            print("Saque não realizado! O valor do saque excede o limite disponível.")
    elif limite_saque_excedido:
        print("Saque não realizado! O limite máximo de tentativas foi alcançado.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Saque não realizado! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================================")

"""
A função criar usuários, foi desenvolvida como uma parte do requisito inicial do desenvolvimento do siste
ma conta bancária. Nela validamos se um cliente já existe na base de dados, se existir uma menssagem com 
um tratamento de excessão é apresentado retornando o primeiro usuário válido. Caso contrário. 
"""
def criar_usuario(usuarios):
    cpf = input("Digite o CPF do novo usuário: ")
    nome = input("Digite o Nome do novo usuário")
    data_nascimento = input("Insira a data de nascimento no formato (dd/mm/aaaa): ")
    endereco = input("Insira o endereço no formato(logradouro, nro - bairro - cidade/sigla estado): ")
    senha = input("Digite a senha do novo usuário: ")

    if validar_usuario(usuarios, cpf, senha):
        print("CPF já existe. Não é possível criar um usuário duplicado.")
    else:
        novo_usuario = {"cpf": cpf, "nome": nome, "data_nascimento":data_nascimento, "endereco":endereco, "senha": senha}
        usuarios.append(novo_usuario)
        print("Novo usuário criado com sucesso!")

def validar_usuario(usuarios, cpf, senha):
    usuario_validado = [usuario for usuario in usuarios if usuario["cpf"] == cpf and usuario["senha"] == senha]
    return usuario_validado[0] if usuario_validado else None

def listar_usuarios(usuarios):
    print("\nLista de Usuários:")
    for idx, usuario in enumerate(usuarios, start=1):
        print(f"{idx}. CPF: {usuario['cpf']}")
        
"""
A função obter próximo número de contas, foi desenvolvida como um parte opcional em relação ao requisito 
inicial do projeto. No entanto o desenvolvimento mostra que há infinitas possibilidades de melhoria no 
código. Esta função garante que o próximo número de conta seja único e incremental.
"""
def obter_proximo_numero_conta(contas):
    numeros_contas = [conta["numero_conta"] for conta in contas]
    proximo_numero = max(numeros_contas, default=0) + 1
    return proximo_numero

"""
A função criar contas, foi desenvolvida como uma parte do requisito inicial do desenvolvimento do sistema
conta bancária. Nela validamos se um cliente já existe na base de dados, caso contrário uma menssagem com
um tratamento de excessão é apresentado retornando vazio. Se o usuário for encontrado na base de dados a
função valida o primeiro usuário criando uma nova conta, associando ao CPF já existente.
"""
def criar_conta(agencia, contas, usuarios):
    cpf = input("Digite o CPF do titular da nova conta: ")
    senha = input("Digite a senha do titular: ")

    usuario = validar_usuario(usuarios, cpf, senha)
    if usuario:
        numero_conta = obter_proximo_numero_conta(contas)
        nova_conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        print("Nova conta criada com sucesso!")
        return nova_conta
    else:
        print("Usuário inválido ou senha incorreta. Não é possível criar a conta.")
        return None

def listar_contas(contas):
    for conta in contas:
        linha = (
            f"Agência:\t{conta['agencia']}\n"
            f"C/C:\t\t{conta['numero_conta']}\n"
            f"Titular:\t{conta['usuario']['nome']}"
        )
        print("=" * 100)
        print(linha)

"""
A função encerrar contas, foi desenvolvida como um parte opcional em relação ao requisito 
inicial do projeto. No entanto o desenvolvimento mostra que há infinitas possibilidades de
melhoria no código.
"""
def encerrar_conta(contas, numero_conta):
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            contas.remove(conta)
            print("Conta encerrada com sucesso!")
            return
    print("Conta não encontrada.")

def menu():
    return input(menu_text)

def menu_principal():
    saldo = 0
    valor_limite_saque = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo = saldo, 
                valor = valor, 
                extrato = extrato, 
                valor_limite_saque = valor_limite_saque, 
                numero_saques = numero_saques, 
                limite_saques = LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, contas, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "ec":
            numero_conta = int(input("Digite o número da conta que deseja encerrar: "))
            encerrar_conta(contas, numero_conta)
            
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

menu_text = """\n
================ MENU =================
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova conta
[lc]\tListar contas
[nu]\tNovo usuário
[lu]\tListar usuários
[ec]\tEncerrar conta
[q]\tSair
=> """

menu_principal()