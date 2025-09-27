from typing import Literal
from pydantic import Field
from schemaorg_models.educational_organization import EducationalOrganization


class CollegeOrUniversity(EducationalOrganization):
    """
A college, university, or other third-level educational institution.
    """
    class_: Literal['https://schema.org/CollegeOrUniversity'] = Field(default='https://schema.org/CollegeOrUniversity', alias='class', serialization_alias='class') # type: ignore
