from typing import Literal
from pydantic import Field
from schemaorg_models.administrative_area import AdministrativeArea


class Country(AdministrativeArea):
    """
A country.
    """
    type_: Literal['https://schema.org/Country'] = Field(default='https://schema.org/Country', alias='@type', serialization_alias='@type') # type: ignore
