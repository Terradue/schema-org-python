from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoRental(AutomotiveBusiness):
    """
A car rental business.
    """
    class_: Literal['https://schema.org/AutoRental'] = Field('class', alias='class', serialization_alias='class') # type: ignore
