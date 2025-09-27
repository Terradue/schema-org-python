from typing import Literal
from pydantic import Field
from schemaorg_models.intangible import Intangible


class Quantity(Intangible):
    """
Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 kg' or '4 milligrams'.
    """
    type_: Literal['https://schema.org/Quantity'] = Field(default='https://schema.org/Quantity', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
