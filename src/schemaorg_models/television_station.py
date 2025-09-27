from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class TelevisionStation(LocalBusiness):
    """
A television station.
    """
    type_: Literal['https://schema.org/TelevisionStation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TelevisionStation'),serialization_alias='class') # type: ignore
