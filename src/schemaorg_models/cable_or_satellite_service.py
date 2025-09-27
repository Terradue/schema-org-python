from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.service import Service


class CableOrSatelliteService(Service):
    """
A service which provides access to media programming like TV or radio. Access may be via cable or satellite.
    """
    type_: Literal['https://schema.org/CableOrSatelliteService'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CableOrSatelliteService'),serialization_alias='class') # type: ignore
