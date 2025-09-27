from typing import Literal
from pydantic import Field
from schemaorg_models.administrative_area import AdministrativeArea


class Country(AdministrativeArea):
    """
A country.
    """
    class_: Literal['https://schema.org/Country'] = Field('class', alias='class', serialization_alias='class') # type: ignore
