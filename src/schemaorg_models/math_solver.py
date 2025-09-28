from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .solve_math_action import SolveMathAction

class MathSolver(CreativeWork):
    """
A math solver which is capable of solving a subset of mathematical problems.
    """
    class_: Literal['https://schema.org/MathSolver'] = Field( # type: ignore
        default='https://schema.org/MathSolver',
        alias='@type',
        serialization_alias='@type'
    )
    mathExpression: Optional[Union["SolveMathAction", List["SolveMathAction"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mathExpression',
            'https://schema.org/mathExpression'
        ),
        serialization_alias='https://schema.org/mathExpression'
    )
