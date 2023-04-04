import ast
from typing import Any

UNARY_OPS = (ast.UAdd, ast.USub, ast.UnaryOp)
BINARY_OPS = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod)


def is_arithmetic(s: str) -> bool:
    def _is_arithmetic(node: Any) -> bool:
        if isinstance(node, ast.Num):
            return True
        elif isinstance(node, ast.Expression):
            return _is_arithmetic(node.body)
        elif isinstance(node, ast.UnaryOp):
            valid_op = isinstance(node.op, UNARY_OPS)
            return valid_op and _is_arithmetic(node.operand)
        elif isinstance(node, ast.BinOp):
            valid_op = isinstance(node.op, BINARY_OPS)
            return valid_op and _is_arithmetic(node.left) and _is_arithmetic(node.right)
        else:
            raise ValueError('Unsupported type {}'.format(node))

    try:
        return _is_arithmetic(ast.parse(s, mode='eval'))
    except (SyntaxError, ValueError):
        return False


def exec_operation(op: str) -> float:
    if not is_arithmetic(op):
        raise ValueError('Operação não é aritmética! Não é possível resolver esse cálculo')

    value_parsed = ast.parse(op, mode='eval')
    value = eval(compile(value_parsed, "", "eval"))

    print('OPERAÇÃO A SER REALIZADA:', ast.unparse(value_parsed))
    print('RESULTADO:', value)

    return value


def isNumber(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False
