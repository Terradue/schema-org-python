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

class RestrictedDiet(Enumeration):
    """
A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons. 
    """
    class_: Literal['https://schema.org/RestrictedDiet'] = Field( # type: ignore
        default='https://schema.org/RestrictedDiet',
        alias='@type',
        serialization_alias='@type'
    )
