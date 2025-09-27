from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class EmergencyService(LocalBusiness):
    """
An emergency service, such as a fire station or ER.
    """
    type_: Literal['https://schema.org/EmergencyService'] = Field(default='https://schema.org/EmergencyService', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
