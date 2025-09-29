from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
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
    '''
    A math solver which is capable of solving a subset of mathematical problems.

    Attributes:
        mathExpression: A mathematical expression (e.g. 'x^2-3x=0') that may be solved for a specific variable, simplified, or transformed. This can take many formats, e.g. LaTeX, Ascii-Math, or math as you would write with a keyboard.
    '''
    class_: Literal['https://schema.org/MathSolver'] = Field( # type: ignore
        default='https://schema.org/MathSolver',
        alias='@type',
        serialization_alias='@type'
    )
    mathExpression: Optional[Union['SolveMathAction', List['SolveMathAction'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mathExpression',
            'https://schema.org/mathExpression'
        ),
        serialization_alias='https://schema.org/mathExpression'
    )
