from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.administrative_area import AdministrativeArea

from pydantic import (
    Field
)
from typing import (
    Literal
)

class City(AdministrativeArea):
    """
A city or town.
    """
    class_: Literal['https://schema.org/City'] = Field( # type: ignore
        default='https://schema.org/City',
        alias='@type',
        serialization_alias='@type'
    )
