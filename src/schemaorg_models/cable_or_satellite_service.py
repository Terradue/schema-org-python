from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.service import Service

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CableOrSatelliteService(Service):
    """
A service which provides access to media programming like TV or radio. Access may be via cable or satellite.
    """
    class_: Literal['https://schema.org/CableOrSatelliteService'] = Field( # type: ignore
        default='https://schema.org/CableOrSatelliteService',
        alias='@type',
        serialization_alias='@type'
    )
