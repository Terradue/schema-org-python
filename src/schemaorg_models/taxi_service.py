from typing import Literal
from pydantic import Field
from schemaorg_models.service import Service


class TaxiService(Service):
    """
A service for a vehicle for hire with a driver for local travel. Fares are usually calculated based on distance traveled.
    """
    type_: Literal['https://schema.org/TaxiService'] = Field(default='https://schema.org/TaxiService', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
