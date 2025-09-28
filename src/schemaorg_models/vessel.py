from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.anatomical_structure import AnatomicalStructure

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Vessel(AnatomicalStructure):
    """
A component of the human body circulatory system comprised of an intricate network of hollow tubes that transport blood throughout the entire body.
    """
    class_: Literal['https://schema.org/Vessel'] = Field( # type: ignore
        default='https://schema.org/Vessel',
        alias='@type',
        serialization_alias='@type'
    )
