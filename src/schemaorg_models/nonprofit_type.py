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

class NonprofitType(Enumeration):
    """
NonprofitType enumerates several kinds of official non-profit types of which a non-profit organization can be.
    """
    class_: Literal['https://schema.org/NonprofitType'] = Field( # type: ignore
        default='https://schema.org/NonprofitType',
        alias='@type',
        serialization_alias='@type'
    )
