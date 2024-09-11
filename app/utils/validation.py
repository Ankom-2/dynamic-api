import ast


def validate_formula(formula, data_keys, intermediate_keys):
    """
    Validate that the formula expression only uses variables defined in the inputs, present in the data, or produced by other formulas
    """
    try:
        node = ast.parse(formula.expression, mode="eval").body
        for n in ast.walk(node):
            if (
                isinstance(n, ast.Name)
                and n.id not in data_keys
                and n.id not in intermediate_keys
            ):
                raise ValueError(
                    f"variable '{n.id}' in formula '{formula.expression}' is not defined in the inputs, data, or produced by other formulas"
                )
    except Exception as e:
        raise ValueError(
            f"Invalid formula expression: {formula.expression}. Error: {str(e)}"
        )
