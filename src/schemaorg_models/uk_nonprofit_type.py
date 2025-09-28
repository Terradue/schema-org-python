from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.nonprofit_type import NonprofitType

from pydantic import (
    Field
)
from typing import (
    Literal
)

class UKNonprofitType(NonprofitType):
    """
UKNonprofitType: Non-profit organization type originating from the United Kingdom.
    """
    class_: Literal['https://schema.org/UKNonprofitType'] = Field( # type: ignore
        default='https://schema.org/UKNonprofitType',
        alias='@type',
        serialization_alias='@type'
    )
