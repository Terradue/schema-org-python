from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class MathSolver(CreativeWork):
    """
A math solver which is capable of solving a subset of mathematical problems.
    """
    mathExpression: Optional[Union["SolveMathAction", List["SolveMathAction"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('mathExpression', 'https://schema.org/mathExpression'),serialization_alias='https://schema.org/mathExpression')
