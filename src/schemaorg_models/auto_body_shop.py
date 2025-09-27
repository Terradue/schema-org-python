from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoBodyShop(AutomotiveBusiness):
    """
Auto body shop.
    """
    type_: Literal['https://schema.org/AutoBodyShop'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AutoBodyShop'),serialization_alias='class') # type: ignore
