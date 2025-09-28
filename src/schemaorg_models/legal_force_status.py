from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.status_enumeration import StatusEnumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class LegalForceStatus(StatusEnumeration):
    """
A list of possible statuses for the legal force of a legislation.
    """
    class_: Literal['https://schema.org/LegalForceStatus'] = Field( # type: ignore
        default='https://schema.org/LegalForceStatus',
        alias='@type',
        serialization_alias='@type'
    )
