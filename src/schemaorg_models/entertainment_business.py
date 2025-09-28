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

class EntertainmentBusiness(LocalBusiness):
    """
A sub property of location. The entertainment business where the action occurred.
    """
    class_: Literal['https://schema.org/EntertainmentBusiness'] = Field( # type: ignore
        default='https://schema.org/EntertainmentBusiness',
        alias='@type',
        serialization_alias='@type'
    )
