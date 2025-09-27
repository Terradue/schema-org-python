from typing import Literal
from pydantic import Field
from schemaorg_models.service import Service


class TaxiService(Service):
    """
A service for a vehicle for hire with a driver for local travel. Fares are usually calculated based on distance traveled.
    """
    class_: Literal['https://schema.org/TaxiService'] = Field(default='https://schema.org/TaxiService', alias='@type', serialization_alias='@type') # type: ignore
