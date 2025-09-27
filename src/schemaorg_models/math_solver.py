from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class MathSolver(CreativeWork):
    """
A math solver which is capable of solving a subset of mathematical problems.
    """
    class_: Literal['https://schema.org/MathSolver'] = Field(default='https://schema.org/MathSolver', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    mathExpression: Optional[Union["SolveMathAction", List["SolveMathAction"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('mathExpression', 'https://schema.org/mathExpression'), serialization_alias='https://schema.org/mathExpression')
