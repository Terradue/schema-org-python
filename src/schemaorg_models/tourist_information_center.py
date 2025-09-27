from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class TouristInformationCenter(LocalBusiness):
    """
A tourist information center.
    """
    type_: Literal['https://schema.org/TouristInformationCenter'] = Field(default='https://schema.org/TouristInformationCenter', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
