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

    def scan_result(self, token_type: str, lexeme: str | float) -> None:
        print(f'Token [type={token_type}, lexeme={lexeme}]')

    def exec_op(self, op: str, *nums: str) -> None:
        if op == '^':
            op = '**'

        operation = op.join(reversed(nums))
        is_arithmetic_op, operator_type = misc.is_arithmetic(operation)
        if is_arithmetic_op:
            self.scan_result(token_type=operator_type, lexeme=op)
            self.stack.append(str(misc.exec_operation(operation)))
        else:
            raise ValueError(
                f'A operação `{operation}` não é uma operação aritmética válida!', f'Unexpected character: {op}'
            )

    def read_file(self, mode: str = 'r') -> None:
        with open(self.file_path, mode) as f:
            step = 0
            for line in f:
                step += 1
                print('-' * 30, 'STEP', step, '-' * 30)

                # Remover possíveis espaços em branco antes e depois do elemento na linha
                element = line.strip()
                if misc.is_number(element):
                    self.scan_result(token_type='NUM', lexeme=float(element))
                    self.stack.append(element)
                elif misc.is_operator(element):
                    try:
                        num1 = self.stack.pop()
                        num2 = self.stack.pop()
                        self.exec_op(element, num1, num2)
                    except IndexError:
                        raise SyntaxError(NON_ACCEPTABLE_FILE_ERROR)
                else:
                    raise ValueError(f'Unexpected character: {element}')

    def execute_task(self) -> None:
        self.read_file()
        if self.__stack_is_empty() or len(self.stack) != 1:
            raise SyntaxError(NON_ACCEPTABLE_FILE_ERROR)

        final_result = self.stack.pop()
        if not misc.is_number(final_result):
            raise ValueError(f'Valor: {final_result} não pôde ser transformado em número.')

        print('\n')
        print('RESULTADO FINAL =', final_result)


if __name__ == '__main__':
    task = Task(file_path=FILE_PATH)
    try:
        task.execute_task()
    except:
        print_exc()
