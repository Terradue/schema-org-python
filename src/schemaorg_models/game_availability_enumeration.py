from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.enumeration import Enumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class GameAvailabilityEnumeration(Enumeration):
    """
For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind of game availability offered. 
    """
    class_: Literal['https://schema.org/GameAvailabilityEnumeration'] = Field( # type: ignore
        default='https://schema.org/GameAvailabilityEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
