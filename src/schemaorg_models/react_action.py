from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.assess_action import AssessAction


class ReactAction(AssessAction):
    """
The act of responding instinctively and emotionally to an object, expressing a sentiment.
    """
    type_: Literal['https://schema.org/ReactAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ReactAction'),serialization_alias='class') # type: ignore
