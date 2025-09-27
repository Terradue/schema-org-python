from typing import Literal
from pydantic import Field
from schemaorg_models.service import Service


class Taxi(Service):
    """
A taxi.
    """
    class_: Literal['https://schema.org/Taxi'] = Field(default='https://schema.org/Taxi', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
