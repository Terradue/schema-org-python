from typing import Literal
from pydantic import Field
from schemaorg_models.administrative_area import AdministrativeArea


class State(AdministrativeArea):
    """
A state or province of a country.
    """
    class_: Literal['https://schema.org/State'] = Field('class', alias='class', serialization_alias='class') # type: ignore
