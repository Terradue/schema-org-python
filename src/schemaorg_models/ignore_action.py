from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.assess_action import AssessAction


class IgnoreAction(AssessAction):
    """
The act of intentionally disregarding the object. An agent ignores an object.
    """
    type_: Literal['https://schema.org/IgnoreAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/IgnoreAction'),serialization_alias='class') # type: ignore
