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

class DigitalDocumentPermissionType(Enumeration):
    """
A type of permission which can be granted for accessing a digital document.
    """
    class_: Literal['https://schema.org/DigitalDocumentPermissionType'] = Field( # type: ignore
        default='https://schema.org/DigitalDocumentPermissionType',
        alias='@type',
        serialization_alias='@type'
    )
