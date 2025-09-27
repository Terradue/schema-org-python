from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.administrative_area import AdministrativeArea


class State(AdministrativeArea):
    """
A state or province of a country.
    """
    type_: Literal['https://schema.org/State'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/State'),serialization_alias='class') # type: ignore
