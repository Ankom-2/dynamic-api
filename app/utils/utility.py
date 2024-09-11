import re
import ast
from datetime import datetime
import operator
from collections import defaultdict, deque

# Supported operators:
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.BitXor: operator.xor,
    ast.USub: operator.neg,
}


def parse_value(value, var_type):
    """
    Parse the value based on its type.
    """

    if var_type == "number":
        return float(value)
    elif var_type == "currency":
        return float(re.sub(r"[^\d.]", "", value))
    elif var_type == "percentage":
        return float(value.strip("%")) / 100
    elif var_type == "boolean":
        return bool(value)
    elif var_type == "datetime":
        return datetime.fromisoformat(value)
    else:
        raise ValueError(f"Unsupported variable type: {var_type}")


def eval_expr(expr, data):
    """Evaluate a mathematical expression using the provided data"""
    try:
        node = ast.parse(expr, mode="eval").body
        return eval_(node, data)
    except Exception as e:
        raise ValueError(f"Invalid expression: {expr}. Error: {str(e)}")


def eval_(node, data):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left, data), eval_(node.right, data))
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return operators[type[node.op]](eval_(node.operand, data))
    elif isinstance(node, ast.Name):
        return data[node.id]
    else:
        raise TypeError(node)


def determine_execution_order(formulas):
    """Determine the order of the execution based on formula dependencies"""
    # Build the dependency graph:
    dependencies = defaultdict(set)
    incoming_count = defaultdict(int)
    for formula in formulas:
        output_var = formula.outputVar
        input_vars = {input_var.varName for input_var in formula.inputs}
        dependencies[output_var].update(input_vars)
        for input_var in input_vars:
            incoming_count[input_var] += 1
        if output_var not in incoming_count:
            incoming_count[output_var] = 0

    # Find all nodes with no incoming edges:
    no_incoming = deque([node for node in incoming_count if incoming_count[node] == 0])

    # Using Topological sort to identify the cycle and execution order:
    execution_order = []
    while no_incoming:
        node = no_incoming.popleft()
        execution_order.append(node)
        for dependent in dependencies[node]:
            incoming_count[dependent] -= 1
            if incoming_count[dependent] == 0:
                no_incoming.append(dependent)
        dependencies.pop(node)

    if len(execution_order) != len(incoming_count):
        raise ValueError("A cyclic dependency occured in the formulas.")
    return execution_order
