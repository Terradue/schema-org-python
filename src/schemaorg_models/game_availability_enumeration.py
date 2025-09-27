from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class GameAvailabilityEnumeration(Enumeration):
    """
For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind of game availability offered. 
    """
    class_: Literal['https://schema.org/GameAvailabilityEnumeration'] = Field(default='https://schema.org/GameAvailabilityEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
