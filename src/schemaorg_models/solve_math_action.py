from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class SolveMathAction(Action):
    """
The action that takes in a math expression and directs users to a page potentially capable of solving/simplifying that expression.
    """
    class_: Literal['https://schema.org/SolveMathAction'] = Field(default='https://schema.org/SolveMathAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    eduQuestionType: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('eduQuestionType', 'https://schema.org/eduQuestionType'), serialization_alias='https://schema.org/eduQuestionType')
