from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class SolveMathAction(Action):
    """
The action that takes in a math expression and directs users to a page potentially capable of solving/simplifying that expression.
    """
    class_: Literal['https://schema.org/SolveMathAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    eduQuestionType: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('eduQuestionType', 'https://schema.org/eduQuestionType'), serialization_alias='https://schema.org/eduQuestionType')
