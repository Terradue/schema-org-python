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

class State(AdministrativeArea):
    """
A state or province of a country.
    """
    class_: Literal['https://schema.org/State'] = Field( # type: ignore
        default='https://schema.org/State',
        alias='@type',
        serialization_alias='@type'
    )
