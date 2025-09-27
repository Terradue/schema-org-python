from typing import Literal
from pydantic import Field
from schemaorg_models.service import Service


class Taxi(Service):
    """
A taxi.
    """
    type_: Literal['https://schema.org/Taxi'] = Field(default='https://schema.org/Taxi', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
