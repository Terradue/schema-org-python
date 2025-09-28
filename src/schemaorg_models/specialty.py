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

class Specialty(Enumeration):
    """
One of the domain specialities to which this web page's content applies.
    """
    class_: Literal['https://schema.org/Specialty'] = Field( # type: ignore
        default='https://schema.org/Specialty',
        alias='@type',
        serialization_alias='@type'
    )
