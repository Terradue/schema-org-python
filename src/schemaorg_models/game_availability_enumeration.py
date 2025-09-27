from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class GameAvailabilityEnumeration(Enumeration):
    """
For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind of game availability offered. 
    """
    type_: Literal['https://schema.org/GameAvailabilityEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GameAvailabilityEnumeration'),serialization_alias='class') # type: ignore
