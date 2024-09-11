from pydantic import BaseModel, field_validator
from typing import List, Dict, Any


class InputVar(BaseModel):
    varName: str
    varType: str

    @field_validator("varType")
    def validate_var_type(cls, v):
        if v not in {"number", "currency", "percentage", "boolean", "datetime"}:
            raise ValueError(
                "VarType must be 'number', 'currency', 'percentage', 'boolean', or 'datetime'"
            )
        return v


class Formula(BaseModel):
    outputVar: str
    expression: str
    inputs: List[InputVar]


class Payload(BaseModel):
    data: List[Dict[str, Any]]
    formulas: List[Formula]
