from typing import Literal
from pydantic import Field
from schemaorg_models.intangible import Intangible


class Quantity(Intangible):
    """
Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 kg' or '4 milligrams'.
    """
    class_: Literal['https://schema.org/Quantity'] = Field('class', alias='class', serialization_alias='class') # type: ignore
