from re import compile
from traceback import print_exc
from typing import List, Tuple
from collections import deque
from utils import misc

FILE_PATH = 'files/Calc.stk'
NON_ACCEPTABLE_FILE_ERROR = 'Não foi possível realizar esse cálculo. É bem provável que a formatação do arquivo de entrada esteja errada. Verifique-o e tente novamente!'
ALL_OPS = "'+''-''*''/''^''**'"


class Regex:
    def __init__(self, element: str) -> None:
        # Remover possíveis espaços em branco antes e depois do elemento na linha
        self.element: str = element.strip()

    def is_number(self) -> bool:
        num_regex = compile(r'^\d+(?:,\d*)?$')
        result = num_regex.match(self.element)

        return result is not None

    def is_operator(self) -> bool:
        op_regex = compile(rf'^[{ALL_OPS}]$')
        result = op_regex.match(self.element)

        return result is not None


class Task:
    def __init__(self, file_path: str) -> None:
        self.stack: deque = deque()
        self.file_path: str = file_path
        self.scan_result_list: List[str] = []

    def __stack_is_empty(self) -> bool:
        return not bool(self.stack)

    def scan_result(self, token_type: str, lexeme: str | float) -> None:
        self.scan_result_list.append(f'Token [type={token_type}, lexeme={lexeme}]')

    def exec_op(self, op: str, *nums: Tuple[str]) -> None:
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
            for line in f:
                reg_value = Regex(line)
                if reg_value.is_number():
                    self.scan_result(token_type='NUM', lexeme=float(reg_value.element))
                    self.stack.append(reg_value.element)
                elif reg_value.is_operator():
                    try:
                        num1 = self.stack.pop()
                        num2 = self.stack.pop()
                        self.exec_op(reg_value.element, num1, num2)
                    except IndexError:
                        raise SyntaxError(NON_ACCEPTABLE_FILE_ERROR)
                else:
                    raise ValueError(f'Unexpected character: {reg_value.element}')

    def execute_task(self) -> None:
        self.read_file()
        if self.__stack_is_empty() or len(self.stack) != 1:
            raise SyntaxError(NON_ACCEPTABLE_FILE_ERROR)

        final_result = self.stack.pop()

        for sr in self.scan_result_list:
            print(sr)
        print('\n')
        print('RESULTADO FINAL =', final_result)


if __name__ == '__main__':
    task = Task(file_path=FILE_PATH)
    try:
        task.execute_task()
    except:
        print_exc()
