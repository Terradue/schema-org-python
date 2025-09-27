from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.administrative_area import AdministrativeArea


class SchoolDistrict(AdministrativeArea):
    """
A School District is an administrative area for the administration of schools.
    """
    type_: Literal['https://schema.org/SchoolDistrict'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SchoolDistrict'),serialization_alias='class') # type: ignore
