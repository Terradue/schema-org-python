from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.place import Place

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AdministrativeArea(Place):
    """
A geographical region, typically under the jurisdiction of a particular government.
    """
    class_: Literal['https://schema.org/AdministrativeArea'] = Field( # type: ignore
        default='https://schema.org/AdministrativeArea',
        alias='@type',
        serialization_alias='@type'
    )
