from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.local_business import LocalBusiness

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TouristInformationCenter(LocalBusiness):
    """
A tourist information center.
    """
    class_: Literal['https://schema.org/TouristInformationCenter'] = Field( # type: ignore
        default='https://schema.org/TouristInformationCenter',
        alias='@type',
        serialization_alias='@type'
    )
