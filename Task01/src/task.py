from traceback import print_exc
from collections import deque
from utils import misc

FILE_PATH = 'files/Calc.stk'
NON_ACCEPTABLE_FILE_ERROR = 'Não foi possível realizar esse cálculo. É bem provável que a formatação do arquivo de entrada esteja errada. Verifique-o e tente novamente!'


class Task:
    def __init__(self, file_path: str) -> None:
        self.stack: deque = deque()
        self.file_path: str = file_path

    def __stack_is_empty(self) -> bool:
        return not bool(self.stack)

    def exec_op(self, op: str, *nums: str) -> None:
        if not op or not nums or len(nums) < 2:
            return

        operation = op.join(reversed(nums))
        self.stack.append(str(misc.exec_operation(operation)))

    def read_file(self, mode: str = 'r') -> None:
        with open(self.file_path, mode) as f:
            for line in f:
                # Remover possíveis espaços em branco antes e depois do elemento na linha
                element = line.strip()
                if misc.is_number(element):
                    self.stack.append(element)
                else:
                    try:
                        num1 = self.stack.pop()
                        num2 = self.stack.pop()
                        self.exec_op(element, num1, num2)
                    except IndexError:
                        raise SyntaxError(NON_ACCEPTABLE_FILE_ERROR)

    def execute_task(self) -> None:
        self.read_file()
        if self.__stack_is_empty() or len(self.stack) != 1:
            raise SyntaxError(NON_ACCEPTABLE_FILE_ERROR)

        final_result = self.stack.pop()
        if not misc.is_number(final_result):
            raise ValueError(f'Valor: {final_result} não pôde ser transformado em número.')

        print('-' * 25, 'RESULTADO FINAL', '-' * 25)
        print(final_result)


if __name__ == '__main__':
    task = Task(file_path=FILE_PATH)
    try:
        task.execute_task()
    except:
        print_exc()
