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

class MapCategoryType(Enumeration):
    """
An enumeration of several kinds of Map.
    """
    class_: Literal['https://schema.org/MapCategoryType'] = Field( # type: ignore
        default='https://schema.org/MapCategoryType',
        alias='@type',
        serialization_alias='@type'
    )
