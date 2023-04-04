# Task 02 - RPNStacker Manual/Simple Scanning

Evoluir o projeto da Task 01 para implementar uma feature de scanning.

A entrada consiste num arquivo `.stk` (ver arquivo `files/Calc.stk`), onde cada elemento é separado por quebras de linha.

Para mudar a entrada sem alterar o código, basta realizar as mudanças diretamente no arquivo citado acima.

## Dependências

- Python v3.11.0
- Poetry v1.4.2 _(opcional)_

## Como testar o programa localmente

Considerando que você possui a versão de [python](https://www.python.org/downloads/) indicada instalada e o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/installation/):

1. Instalação das bibliotecas necessárias

   _Obs: nessa task não foi necessária a instalação de nenhuma biblioteca não padrão. Logo, esse step pode ser pulado._

   ```bash
   pip install "poetry==1.4.2"
   poetry config virtualenvs.create false && poetry install --no-ansi --no-interaction --only main
   ```

2. Executar a task

   ```bash
   cd src/ && python task.py
   ```
