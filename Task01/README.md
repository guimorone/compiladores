# Task 01 - RPNStacker Adhoc

Implementar uma linguagem RPN stacker em Python usando uma pilha como estrutura de dados.

A entrada consiste num arquivo `.stk` (ver arquivo `files/Calc.stk`), onde cada elemento é separado por quebras de linha.

Para mudar a entrada sem alterar o código, basta realizar as mudanças diretamente no arquivo citado acima.

## Dependências

- Python v3.11.0
- Poetry v1.4.2

## Como testar o programa localmente

Considerando que você possui a versão de [python](https://www.python.org/downloads/) indicada instalada e o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/installation/):

1. Instalação das bibliotecas necessárias

   Obs: nessa task não foi necessária a instalação de nenhuma biblioteca não padrão. Logo, esse step pode ser pulado.

   ```bash
   pip install "poetry==1.4.2"
   poetry config virtualenvs.create false && poetry install --no-ansi --no-interaction --only main
   ```

2. Executar a task

   ```bash
   cd src/ && python task.py
   ```
