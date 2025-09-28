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

class StatusEnumeration(Enumeration):
    """
Lists or enumerations dealing with status types.
    """
    class_: Literal['https://schema.org/StatusEnumeration'] = Field( # type: ignore
        default='https://schema.org/StatusEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
