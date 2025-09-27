from typing import Literal
from pydantic import Field
from schemaorg_models.administrative_area import AdministrativeArea


class City(AdministrativeArea):
    """
A city or town.
    """
    type_: Literal['https://schema.org/City'] = Field(default='https://schema.org/City', alias='@type', serialization_alias='@type') # type: ignore
