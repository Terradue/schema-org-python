from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.find_action import FindAction


class CheckAction(FindAction):
    """
An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.
    """
    type_: Literal['https://schema.org/CheckAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CheckAction'),serialization_alias='class') # type: ignore
