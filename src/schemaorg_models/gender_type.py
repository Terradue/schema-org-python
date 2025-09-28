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

class GenderType(Enumeration):
    """
An enumeration of genders.
    """
    class_: Literal['https://schema.org/GenderType'] = Field( # type: ignore
        default='https://schema.org/GenderType',
        alias='@type',
        serialization_alias='@type'
    )
