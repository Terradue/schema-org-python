from typing import Literal
from pydantic import Field
from schemaorg_models.administrative_area import AdministrativeArea


class SchoolDistrict(AdministrativeArea):
    """
A School District is an administrative area for the administration of schools.
    """
    type_: Literal['https://schema.org/SchoolDistrict'] = Field(default='https://schema.org/SchoolDistrict', alias='@type', serialization_alias='@type') # type: ignore
