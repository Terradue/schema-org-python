from typing import Literal
from pydantic import Field
from schemaorg_models.service import Service


class CableOrSatelliteService(Service):
    """
A service which provides access to media programming like TV or radio. Access may be via cable or satellite.
    """
    class_: Literal['https://schema.org/CableOrSatelliteService'] = Field(default='https://schema.org/CableOrSatelliteService', alias='@type', serialization_alias='@type') # type: ignore
