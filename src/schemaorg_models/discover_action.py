from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.find_action import FindAction


class DiscoverAction(FindAction):
    """
The act of discovering/finding an object.
    """
    type_: Literal['https://schema.org/DiscoverAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DiscoverAction'),serialization_alias='class') # type: ignore
