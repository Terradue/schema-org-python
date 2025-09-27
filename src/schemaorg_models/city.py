from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.administrative_area import AdministrativeArea


class City(AdministrativeArea):
    """
A city or town.
    """
    type_: Literal['https://schema.org/City'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/City'),serialization_alias='class') # type: ignore
