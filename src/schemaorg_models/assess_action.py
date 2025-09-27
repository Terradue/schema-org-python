from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class AssessAction(Action):
    """
The act of forming one's opinion, reaction or sentiment.
    """
    type_: Literal['https://schema.org/AssessAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AssessAction'),serialization_alias='class') # type: ignore
