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

class RadioStation(LocalBusiness):
    """
A radio station.
    """
    class_: Literal['https://schema.org/RadioStation'] = Field( # type: ignore
        default='https://schema.org/RadioStation',
        alias='@type',
        serialization_alias='@type'
    )
