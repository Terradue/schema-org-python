from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.legal_service import LegalService

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Notary(LegalService):
    """
A notary.
    """
    class_: Literal['https://schema.org/Notary'] = Field( # type: ignore
        default='https://schema.org/Notary',
        alias='@type',
        serialization_alias='@type'
    )
