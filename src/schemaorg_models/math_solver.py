from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.creative_work import CreativeWork

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
