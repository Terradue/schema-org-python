from typing import Literal
from pydantic import Field
from schemaorg_models.administrative_area import AdministrativeArea


class SchoolDistrict(AdministrativeArea):
    """
A School District is an administrative area for the administration of schools.
    """
    class_: Literal['https://schema.org/SchoolDistrict'] = Field(default='https://schema.org/SchoolDistrict', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
