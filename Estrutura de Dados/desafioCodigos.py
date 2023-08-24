"""
Este código foi baseado nas sugestões e orientações fornecidas pelo Prof. Guilherme  DIO
sendo parte essencial para o desenolvimendo das atividades do curso Formação Python Deve
loper/Python Developer Training.
Autor: [Vitor Campos]
GitHub: [https://github.com/vitorkol]
Repositório Original: [https://github.com/vitorkol/python-developer-training]
Data: [2023-08-24]
"""
"""
# Desafio 1
Um supermercado está fazendo uma promoção de venda de refrigerantes. Se um dia você comprar
refrigerantes e levar os cascos vazios no dia seguinte, ela troca cada conjunto de K 
garrafas vazias  por uma garrafa cheia. Um cliente quer aproveitar ao máximo essa oferta e 
por isso comprou várias garrafas no primeiro dia da promoção. Agora ele quer saber quantas 
garrafas terá ao final do segundo dia da promoção, se usá-la ao máximo.

Faça um programa para calcular isso.

# Entrada
A primeira linha de entrada contém inteiro T (1 ≤ T ≤ 10000) , que indica o número de casos 
de teste. Em cada uma das T linhas a seguir vêm dois inteiros N e K (1 ≤ K, N ≤ 10000),  
respectivamente o número de refrigerantes comprados e o número de garrafas vazias para ganhar 
uma cheia.

# Saída
Para cada caso de teste imprima o número de garrafas que o cliente terá no segundo dia, se 
aproveitar ao máximo a oferta.

"""
def main():
    # A variável T representa o número de casos de teste
    T = int(input())

    for i in range(T):
        """
        # Inicialmente assumimos que o número de garrafas cheias é o mesmo
        # que o número de garrafas vazias a serem trocadas.
        # Para fazer o split recomendado, se fez necessário usuar a função
        # map(), uma vez que ela tem a capacidade de converter os valores de
        # entrada em inteiros para os calculos abaixo.
        """
        N, K = map(int, input().split())
        
        """
        # O cálculo do total de garrafas após a troca é realizado seguindo
        # a fórmula: total_garrafas_promocao = N // K + N % K;
        # O operador // realiza uma divisão inteira, e N % K calcula o 
        # restante da divisão.
        # A soma desses dois valores resulta no total de garrafas que o 
        # cliente terá ao final do segundo dia.
        """
        total_garrafas_promocao = N // K + N % K
        
        # Impressão formatada para a saída
        print(f'{total_garrafas_promocao}')

if __name__ == "__main__":
    main()
"""
# Desafio 2
Daenerys é a khaleesi dos Dothraki. Juntamente com Drogon, eles vão atrás do Tyrion,
para tentar dominar Westeros. Ela possui, além do seu dragãozinho, um rastreador 
que mede o nível de energia de qualquer ser vivo. Todos os seres com o nível menor 
ou igual a 8000, ela considera como se fosse um inseto. Quando passa deste valor, 
que foi o caso do Drogon, ela se espanta e grita “Mais de 8000”. Baseado nisso, 
utilize a mesma tecnologia e analise o nível de energia dos seres vivos.

# Entrada
A primeira linha contém um número inteiro C relativo ao número de casos de teste. 
Em seguida, haverá C linhas, com um número inteiro N (100 <= N <= 100000) relativo 
ao nível de energia de um ser vivo.

# Saída
Para cada valor lido, imprima o texto correspondente.
"""
def main():
    C = int(input())  # Número de casos de teste

    for i in range(C):
        N = int(input())  # Nível de energia do ser vivo

        if N <= 8000:
            print("Inseto!")
        else:
            print("Mais de 8000!")

if __name__ == "__main__":
    main()

"""
# Desafio 3
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível 
segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos 
animais seguintes foi escolhido, através das três palavras fornecidas.

![imagem desafio](./images//Desafio_intermediario_de_python.png)

# Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o 
animal segundo a figura acima, com todas as letras minúsculas.

# Saída
Imprima o nome do animal correspondente à entrada fornecida.
"""

# Neste exemplo coloquei em prática o uso de dicionário que mapeia as características 
# dos animais e o subconjunto de nomes dos animais.

def main():
    characteristics = {
        "vertebrado": {
            "ave": {
                "carnivoro": "aguia",
                "onivoro": "pomba"
            },
            "mamifero": {
                "onivoro": "homem",
                "herbivoro": "vaca"
            }
        },
        "invertebrado": {
            "inseto": {
                "hematofago": "pulga",
                "herbivoro": "lagarta"
            },
            "anelideo": {
                "hematofago": "sanguessuga",
                "onivoro": "minhoca"
            }
        }
    }
    
    # Leitura das palavras que irão definir as características do animal
    a = input() 
    b = input() 
    c = input() 
    
    # Neste ponto faço um get para acessar o dicionário para obter o nome do animal correspondente
    animal = characteristics[a][b][c]
    print(animal)

if __name__ == "__main__":
    main()