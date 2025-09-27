from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class Quantity(Intangible):
    """
Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 kg' or '4 milligrams'.
    """
    type_: Literal['https://schema.org/Quantity'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Quantity'),serialization_alias='class') # type: ignore
