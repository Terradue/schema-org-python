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

class USNonprofitType(NonprofitType):
    """
USNonprofitType: Non-profit organization type originating from the United States.
    """
    class_: Literal['https://schema.org/USNonprofitType'] = Field( # type: ignore
        default='https://schema.org/USNonprofitType',
        alias='@type',
        serialization_alias='@type'
    )
