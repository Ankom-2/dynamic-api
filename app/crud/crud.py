from schemas.schema import Payload
from fastapi import HTTPException
from utils.validation import validate_formula
from utils.utility import determine_execution_order, parse_value, eval_expr


def run_formula(payload: Payload):
    data_list = payload.data
    formulas = payload.formulas
    results = {formula.outputVar: [] for formula in formulas}
    errors = []

    # Validate the formula and collect intermediate keys:
    data_keys = set(data_list[0].keys())
    intermediate_keys = validate_formulas(formulas, data_keys)
    try:
        execution_order = get_execution_order(formulas)
        print(execution_order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    is_chaining = check_chaining(formulas, intermediate_keys)

    for data in data_list:
        local_data = data.copy()
        for formula in formulas:
            if formula.outputVar in execution_order:
                parse_and_evaluate(formula, local_data, results, errors)

    if errors:
        raise HTTPException(
            status_code=400,
            detail={
                "results": results,
                "status": "partial_success",
                "message": "some formulas failed to execute.",
                "errors": errors,
            },
        )
    message = (
        "The formulas were executed successfully with variable-based chaining"
        if is_chaining
        else "The formulas were executed successfully"
    )

    return {"results": results, "status": "success", "message": message}


def validate_formulas(formulas, data_keys):
    intermediate_keys = set()
    for formula in formulas:
        validate_formula(formula, data_keys, intermediate_keys)
        intermediate_keys.add(formula.outputVar)
    return intermediate_keys


def get_execution_order(formulas):
    return determine_execution_order(formulas)


def check_chaining(formulas, intermediate_keys):
    return any(
        input_var.varName in intermediate_keys
        for formula in formulas
        for input_var in formula.inputs
    )


def parse_and_evaluate(formula, local_data, results, errors):
    try:
        for input_var in formula.inputs:
            var_name = input_var.varName
            var_type = input_var.varType
            local_data[var_name] = parse_value(local_data[var_name], var_type)
        result = eval_expr(formula.expression, local_data)
        results[formula.outputVar].append(result)
        local_data[formula.outputVar] = result
    except Exception as e:
        errors.append(
            {"formula": formula.expression, "error": str(e), "data": local_data}
        )
