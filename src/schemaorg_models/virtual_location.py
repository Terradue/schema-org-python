from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.intangible import Intangible

from pydantic import (
    Field
)
from typing import (
    Literal
)

class VirtualLocation(Intangible):
    """
An online or virtual location for attending events. For example, one may attend an online seminar or educational event. While a virtual location may be used as the location of an event, virtual locations should not be confused with physical locations in the real world.
    """
    class_: Literal['https://schema.org/VirtualLocation'] = Field( # type: ignore
        default='https://schema.org/VirtualLocation',
        alias='@type',
        serialization_alias='@type'
    )
