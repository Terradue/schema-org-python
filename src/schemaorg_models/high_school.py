from typing import Literal
from pydantic import Field
from schemaorg_models.educational_organization import EducationalOrganization


class HighSchool(EducationalOrganization):
    """
A high school.
    """
    class_: Literal['https://schema.org/HighSchool'] = Field(default='https://schema.org/HighSchool', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
