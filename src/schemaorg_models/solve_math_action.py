from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class SolveMathAction(Action):
    """
The action that takes in a math expression and directs users to a page potentially capable of solving/simplifying that expression.
    """
    eduQuestionType: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('eduQuestionType', 'https://schema.org/eduQuestionType'),serialization_alias='https://schema.org/eduQuestionType')
