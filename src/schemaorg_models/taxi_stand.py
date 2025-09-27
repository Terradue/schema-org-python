from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class TaxiStand(CivicStructure):
    """
A taxi stand.
    """
    type_: Literal['https://schema.org/TaxiStand'] = Field(default='https://schema.org/TaxiStand', alias='@type', serialization_alias='@type') # type: ignore
