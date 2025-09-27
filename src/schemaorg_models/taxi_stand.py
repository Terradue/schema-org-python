from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class TaxiStand(CivicStructure):
    """
A taxi stand.
    """
    type_: Literal['https://schema.org/TaxiStand'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TaxiStand'),serialization_alias='class') # type: ignore
