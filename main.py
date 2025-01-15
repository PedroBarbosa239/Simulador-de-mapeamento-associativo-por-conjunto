#Nome: Pedro Barbosa de Souza

from math import log2
import random

# define algumas  constantes
TAMANHO_MEMORIA_PRINCIPAL = 0
TAMANHO_BLOCO = 0
TAMANHO_CACHE = 0
LINHAS_POR_CONJUNTO_CACHE = 0

# variaveis para o endereço
tamanho_palavra = 4
w = 0
s = 0
d = 0
bits_tag = 0


#   A classe MemoriaPrincipal simula a memória principal do sistema. Então no construtor  a memória principal é inicializada com blocos,
#onde cada bloco contém palavras aleatórias por conta da função random.
#   A função ler() recebe um endereço e calcula o índice do bloco correspondente na memória, retornando as informações do bloco.
class MemoriaPrincipal:
    def __init__(self):
        self.blocos = [[random.randint(0, 255) for _ in range(TAMANHO_BLOCO // tamanho_palavra)] for _ in range(2 ** s)]

    def ler(self, endereco):
        indice_bloco = (endereco >> w) & ((1 << s) - 1)
        return self.blocos[indice_bloco]



#    A classe LinhaCache é uma linha individual na cache. Então no construtor , cada linha é inicializada com uma tag nula, dados vazios e
#com um contador de uso no zero.
class LinhaCache:
    def __init__(self):
        self.tag = None
        self.dados = [0] * (TAMANHO_BLOCO // tamanho_palavra)
        self.contador_uso = 0




#    A classe Cache ela é a cache do sistema. No construtor, a cache é inicializada com conjuntos de linhas de tamanho x especificado
# A função acessar() recebe um endereço decimal e calcula o índice do conjunto e a tag correspondentes, ele tenta encontrar a linha com
#a tag correspondente no conjunto e retorna os dados se encontrar. Se não encontrar, busca uma linha vazia para armazenar os dados, mas se
#o conjunto estiver cheio, aplica o algoritmo de substituição para substituir a linha menos usada LinhaCache.contador_uso.
class Cache:
    def __init__(self):
        self.conjuntos = [[LinhaCache() for _ in range(LINHAS_POR_CONJUNTO_CACHE)] for _ in range(2 ** d)]
        self.contador_acertos = 0
        self.contador_falhas = 0
        self.contador_substituicoes = 0

    def acessar(self, endereco):
        indice_conjunto = (endereco >> w) & ((1 << d) - 1)
        tag = (endereco >> (w + d)) & ((1 << bits_tag) - 1)

# Mostrar a linha/conjunto acessado com 2 linhas/1 conjunto antes e depois
        print(f"Acessando endereço: {endereco}")
        print(f"Conjunto: {indice_conjunto}, Tag: {tag}")

        conjunto_inicio = max(0, indice_conjunto - 1)
        conjunto_fim = min(len(self.conjuntos), indice_conjunto + 2)

        for i in range(conjunto_inicio, conjunto_fim):
            print(f"Conjunto {i}:")
            for linha in self.conjuntos[i]:
                print(f"  Tag: {linha.tag}, Dados: {linha.dados}, Contador de Uso: {linha.contador_uso}")
# Procura pela linha com a tag correspondente no conjunto
        for linha in self.conjuntos[indice_conjunto]:
            if linha.tag == tag:
                linha.contador_uso += 1
                self.contador_acertos += 1
                print("Cache hit!")
                return linha.dados

# Caso a linha não seja encontrada, busca-se um espaço vazio no conjunto
        for linha in self.conjuntos[indice_conjunto]:
            if linha.tag is None:
                linha.tag = tag
                linha.dados = memoria_principal.ler(endereco)
                linha.contador_uso = 1
                self.contador_falhas += 1
                print("Cache miss! Linha preenchida.")
                return linha.dados

 # Caso o conjunto esteja cheio, usa o algoritmo de substituição LFU
        linha_menos_usada = min(self.conjuntos[indice_conjunto], key=lambda x: x.contador_uso)
        linha_substituida_tag = linha_menos_usada.tag
        linha_menos_usada.tag = tag
        linha_menos_usada.dados = memoria_principal.ler(endereco)
        linha_menos_usada.contador_uso = 1
        self.contador_falhas += 1
        self.contador_substituicoes += 1
        print(f"Cache ta muito cheia /Linha substituída. Tag antiga: {linha_substituida_tag}, Tag nova: {tag}")
        return linha_menos_usada.dados



#    Aqui nessa função é feita a leitura do arquivo, onde contém 4 linhas com informações da aplicação, configurarei algumas váriaveis global para
#são vitais para a aplicação, pois serão utilizadas em toda a aplicação através enquanto funciona.  Ela tenta abrir e ler o arquivo "dados/entrada.txt".
#Em caso de sucesso, ela lê as informações que estão em 4 linhas, onde através do .readline().strip() consegue pegar as informações da linha.
#caso o arquivo não seja encontrado ou tenha dados inválidos, a função exibe uma mensagem de erro especifica que pode ser FileNotFoundError ou ValueError.
#    Depois de recuperar os dados e armazenar nas váriaveis são calculados os seguintes dados tamanho da memória principal, tamanho do bloco, tamanho da cache
#e número de linhas por conjunto na cache. Em seguida isso é usado para calular o w, s, d e bits_tag.
def ler_arquivo_entrada():
    global TAMANHO_MEMORIA_PRINCIPAL, TAMANHO_BLOCO, TAMANHO_CACHE, LINHAS_POR_CONJUNTO_CACHE, w, s, d, bits_tag

    try:
        with open("dados/entrada.txt", "r") as arquivo:
            TAMANHO_MEMORIA_PRINCIPAL = int(arquivo.readline().strip())
            palavras_por_bloco = int(arquivo.readline().strip())
            TAMANHO_CACHE = int(arquivo.readline().strip())
            LINHAS_POR_CONJUNTO_CACHE = int(arquivo.readline().strip())


            TAMANHO_BLOCO = palavras_por_bloco * tamanho_palavra


            w = int(log2(TAMANHO_BLOCO // tamanho_palavra))
            s = int(log2(TAMANHO_MEMORIA_PRINCIPAL // TAMANHO_BLOCO))
            d = int(log2(TAMANHO_CACHE // (LINHAS_POR_CONJUNTO_CACHE * tamanho_palavra)))
            bits_tag = s - d

            print("Informações lidas do arquivo de entrada:")
            print(f"Tamanho da memória principal: {TAMANHO_MEMORIA_PRINCIPAL} bytes")
            print(f"Tamanho do bloco da memória principal: {TAMANHO_BLOCO} bytes")
            print(f"Tamanho da memória cache: {TAMANHO_CACHE} bytes")
            print(f"Número de linhas por conjunto da cache: {LINHAS_POR_CONJUNTO_CACHE}")
            print(f"w: {w} bits")
            print(f"s: {s} bits")
            print(f"d: {d} bits")
            print(f"Bits de tag: {bits_tag} bits")

    except FileNotFoundError:
        print("Erro: Arquivo de entrada não encontrado.")
    except ValueError:
        print("Erro: Formato inválido no arquivo de entrada.")



#    A função main() tem como objetivo conter o nosso menu, onde primeiramente declaramos duas váriaveis globais a memoria principal e a cache.
#Posteriormente coloquei um laço de repetição, que apenas chegará ao seu fim após o usuário escolher a opção 4, onde vai instaurar um break no laço
#fazendo ele ser interrompido
#    Primeiro é informado quais opções podem ser executadas, onde são:
#        1. ler arquivo de entrada : Mostra dados sobre o arquivo de entrada e as configurações do mapeamento
#        2. Acessar endereço de Memória Principal: Através de um edenreço em Decimal(10) podemos visualizar uma parte da MP
#        3. Acessar endereço da memória cache: Através de um edenreço em Decimal(10) podemos visualizar um conjuntop da cache
#        4. Sair: Como própriamente dito sai do laço e imprime algumas informações sobre a execução do programa
#    No programa configurei para que o usuário primeiro escolha obrigatória mente a opção 1, para que ele visualize as informações sonre o mapeamento
#se não o programa da uma mensagem de erro.

def main():
    global memoria_principal, cache

    memoria_principal = None
    cache = None
    while True:
        print("Menu:")
        print("1. Ler arquivo de entrada")
        print("2. Acessar endereço da memória principal")
        print("3. Acessar endereço da memória cache")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":

            ler_arquivo_entrada()
            memoria_principal = MemoriaPrincipal()
            cache = Cache()
        elif escolha == "2":

            if memoria_principal:
                try:
                    endereco = int(input("Digite o endereço da memória principal: "))
                    dados = memoria_principal.ler(endereco)
                    print(f"Dados lidos: {dados}")
                except ValueError:
                    print("Endereço inválido.")
            else:
                print("Erro: Configure a memória primeiro (opção 1).")
        elif escolha == "3":

            if cache:
                try:
                    endereco = int(input("Digite o endereço da memória principal: "))
                    dados = cache.acessar(endereco)
                    print(f"Dados lidos: {dados}")
                except ValueError:
                    print("Endereço inválido.")
            else:
                print("Erro: Configure a memória primeiro (opção 1).")
        elif escolha == "4":
            if cache:
                total_acessos = cache.contador_acertos + cache.contador_falhas
                taxa_acertos = cache.contador_acertos / total_acessos if total_acessos else 0
                taxa_falhas = cache.contador_falhas

                print(f"Taxa de acertos: {taxa_acertos:.2f}")
                print(f"Taxa de falhas: {taxa_falhas:.2f}")
                print(f"Número de substituições: {cache.contador_substituicoes}")

                break
            else:
                print("Opção inválida. Tente novamente.")


#programa irá começar por aqui, chamando a função main()
if __name__ == "__main__":
    main()

