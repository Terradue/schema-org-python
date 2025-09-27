from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class EntertainmentBusiness(LocalBusiness):
    """
A sub property of location. The entertainment business where the action occurred.
    """
    type_: Literal['https://schema.org/EntertainmentBusiness'] = Field(default='https://schema.org/EntertainmentBusiness', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
