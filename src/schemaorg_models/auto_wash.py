from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoWash(AutomotiveBusiness):
    """
A car wash business.
    """
    type_: Literal['https://schema.org/AutoWash'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AutoWash'),serialization_alias='class') # type: ignore
