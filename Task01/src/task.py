from traceback import print_exc
from collections import deque
from utils import misc

FILE_PATH = 'files/Calc.stk'


class Task:
    def __init__(self, file_path: str) -> None:
        self.stack: deque = deque()
        self.final_op: str = ''
        self.read_file(file_path)

    def read_file(self, file_path: str, mode: str = 'r') -> None:
        with open(file_path, mode) as f:
            for line in f:
                # Remover possíveis espaços em branco antes e depois do elemento na linha
                self.stack.append(line.strip())

    def execute_task(self) -> None:
        numbers, current_op = [], ''
        final_parenthesis = 0

        def __put_value(last_op: bool = False, final_parenthesis: int = 0) -> int:
            if current_op != '' and numbers and len(numbers) > 0:
                add_last_op: bool = not last_op
                if not numbers or not len(numbers):
                    raise Exception('Invalid file')
                if len(numbers) == 1:
                    add_last_op = False
                    self.final_op += f'{numbers[0]}{current_op}('
                else:
                    self.final_op += f'({current_op.join(numbers)})'

                if add_last_op:
                    self.final_op += str(current_op) + '('

                final_parenthesis += 1
                numbers.clear()

            return final_parenthesis

        while not self.__stack_is_empty():
            element: str = self.stack.pop()
            if misc.isNumber(element):
                numbers.append(element)
            else:
                final_parenthesis = __put_value(final_parenthesis=final_parenthesis)
                current_op = element

        __put_value(last_op=True)
        self.final_op += ')' * final_parenthesis
        self.final_op = self.final_op.replace('()', '')
        misc.exec_operation(self.final_op)

    def __stack_is_empty(self) -> bool:
        return not bool(self.stack)


if __name__ == '__main__':
    task = Task(file_path=FILE_PATH)
    try:
        task.execute_task()
    except:
        print_exc()
