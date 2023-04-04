import ast
from typing import Any, Tuple

UNARY_OPS = (ast.UAdd, ast.USub, ast.UnaryOp)
BINARY_OPS = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod)


def is_arithmetic(s: str) -> Tuple[bool, str | None]:
    operator: str | None = None

    def _is_arithmetic(node: Any) -> bool:
        nonlocal operator

        if isinstance(node, ast.Num):
            return True
        elif isinstance(node, ast.Expression):
            return _is_arithmetic(node.body)
        elif isinstance(node, ast.UnaryOp):
            operator = ast.dump(node.op).replace('()', '').upper()

            valid_op = isinstance(node.op, UNARY_OPS)
            return valid_op and _is_arithmetic(node.operand)
        elif isinstance(node, ast.BinOp):
            operator = ast.dump(node.op).replace('()', '').upper()

            valid_op = isinstance(node.op, BINARY_OPS)
            return valid_op and _is_arithmetic(node.left) and _is_arithmetic(node.right)
        else:
            raise ValueError('Unsupported type {}'.format(node))

    try:
        return _is_arithmetic(ast.parse(s, mode='eval')), operator
    except (SyntaxError, ValueError):
        return False, None


def exec_operation(op: str) -> float:
    value_parsed = ast.parse(op, mode='eval')
    value = eval(compile(value_parsed, "", "eval"))

    print('OPERAÇÃO A SER REALIZADA:', ast.unparse(value_parsed))
    print('RESULTADO:', value)

    return value


def is_number(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False
