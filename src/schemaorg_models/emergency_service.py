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

class EmergencyService(LocalBusiness):
    """
An emergency service, such as a fire station or ER.
    """
    class_: Literal['https://schema.org/EmergencyService'] = Field( # type: ignore
        default='https://schema.org/EmergencyService',
        alias='@type',
        serialization_alias='@type'
    )
