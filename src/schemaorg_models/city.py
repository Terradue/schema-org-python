from typing import Literal
from pydantic import Field
from schemaorg_models.administrative_area import AdministrativeArea


class City(AdministrativeArea):
    """
A city or town.
    """
    class_: Literal['https://schema.org/City'] = Field('class', alias='class', serialization_alias='class') # type: ignore
