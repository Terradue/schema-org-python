from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class MathSolver(CreativeWork):
    """
A math solver which is capable of solving a subset of mathematical problems.
    """
    class_: Literal['https://schema.org/MathSolver'] = Field(default='https://schema.org/MathSolver', alias='class', serialization_alias='class') # type: ignore
    mathExpression: Optional[Union["SolveMathAction", List["SolveMathAction"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('mathExpression', 'https://schema.org/mathExpression'), serialization_alias='https://schema.org/mathExpression')
