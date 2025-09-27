from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.administrative_area import AdministrativeArea


class Country(AdministrativeArea):
    """
A country.
    """
    type_: Literal['https://schema.org/Country'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Country'),serialization_alias='class') # type: ignore
