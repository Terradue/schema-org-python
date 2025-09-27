from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoRental(AutomotiveBusiness):
    """
A car rental business.
    """
    type_: Literal['https://schema.org/AutoRental'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AutoRental'),serialization_alias='class') # type: ignore
