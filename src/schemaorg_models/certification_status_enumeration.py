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

class CertificationStatusEnumeration(Enumeration):
    """
Enumerates the different statuses of a Certification (Active and Inactive).
    """
    class_: Literal['https://schema.org/CertificationStatusEnumeration'] = Field( # type: ignore
        default='https://schema.org/CertificationStatusEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
