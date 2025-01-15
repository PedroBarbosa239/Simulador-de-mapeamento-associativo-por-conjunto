
# Simulador de Mapeamento de Memória Cache Associativo por Conjunto

Este projeto é uma simulação de mapeamento de memória cache associativo por conjunto, desenvolvido em Python, como parte de estudos em arquitetura de computadores.

## Tabela de Conteúdos
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Funcionamento](#funcionamento)
- [Dependências](#dependências)
- [Estrutura do Projeto](#estrutura-do-projeto)

## Instalação
Para executar este projeto, você precisa de **Python 3.7+**. Clone este repositório e instale as dependências necessárias:

```bash
git clone https://github.com/seu-repositorio/simulador-cache.git
cd simulador-cache
pip install -r requirements.txt
```

## Como Usar
Execute o script principal do simulador:
```bash
python simulador_cache.py
```

Siga as instruções na interface para definir as configurações de cache e memória.

## Funcionamento
Este simulador permite configurar:
- O número de conjuntos de cache
- O tamanho de cada bloco
- Políticas de substituição (FIFO, LRU, etc.)

O sistema simula o funcionamento do mapeamento associativo por conjunto e exibe o resultado das operações de leitura e escrita na cache, com estatísticas de acertos e falhas.

## Dependências
- [Python](https://www.python.org/downloads/) 3.7 ou superior
- [Numpy](https://numpy.org/) para manipulação de arrays e cálculos matemáticos

Instale as dependências com o comando:
```bash
pip install -r requirements.txt
```

## Estrutura do Projeto
```plaintext
simulador-cache/
├── .idea/
├── dados/
│   └── entrada.txt                  # Entrada de dados
├── main.py                          # Arquivo principal do projeto
├── prompts.md                       # prompt para a documentação
└── README.md                        # Documentação do projeto
```

