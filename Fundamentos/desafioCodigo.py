"""
Este código foi baseado nas sugestões e orientações fornecidas pelo Prof. Guilherme  DIO
sendo parte essencial para o desenolvimendo das atividades do curso Formação Python Deve
loper/Python Developer Training.
Autor: [Vitor Campos]
GitHub: [https://github.com/vitorkol]
Repositório Original: [https://github.com/vitorkol/python-developer-training]
Data: [2023-08-20]
"""


"""
# Desafio 1
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado 
como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

# Entrada
A entrada contém um único valor inteiro.

#Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira 
letra em maiúscula.
"""
def obter_nome_mes(numero_mes):
    # Cria um dicionário para meses do ano com chave e valor.
    months_dict = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    
    return months_dict[numero_mes]

# Lê o valor inteiro do usuário, é necessário realizar o tratamento
# porque o input somente é tratado como string.
numero_mes = int(input())

# Chama a função para obter o nome do mês por extenso
nome_mes = obter_nome_mes(numero_mes)

# Imprime o nome do mês com a primeira letra maiúscula
print(nome_mes)

"""
# DESAFIO 2
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto 
vai caber em um tuíte é sua tarefa.

# Entrada
A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

# Saída
A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem 
até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".
"""
def verificar_tweet(T):
    if 1<= len(T) <= 140:
        return "TWEET"
    else:
        return "MUTE"

# Lê a entrada do usuário
T = input()

# Chama a função para verificar se o texto cabe em um tuíte
resultado = verificar_tweet(T)

# Imprime o resultado
print(resultado)

"""
# Desafio 3
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse 
um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde 
aos últimos dígitos de A.

# Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N 
que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B 
maiores que zero, cada um deles podendo ter até 1000 dígitos.

# Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro
valor, confome exemplo abaixo.

A solução deste problema pode ser resolvida de 
duas maneiras, a primeira e mais simples é uti
lizar o loop for.
a segunda um pouco mais customizada é utilizar
uma função para verificar se o sufixo é o final
de uma string X.
"""
#primeira opção usando o loop for
# Lê o número de casos de teste
N = int(input())

# Loop através de cada caso de teste
for _ in range(N):
    A, B = input().split()
    if A.endswith(B):
        resultado = "encaixa"
    else:
        resultado = "nao encaixa"
    print(resultado)

# Segunda opção usando a função para validar a string
def verifica_encaixe(A, B):
    if A.endswith(B):
        return "encaixa"
    else:
        return "nao encaixa"

# Lê o número de casos de teste
N = int(input())

# Loop através de cada caso de teste
for _ in range(N):
    A, B = input().split()
    resultado = verifica_encaixe(A, B)
    print(resultado)
