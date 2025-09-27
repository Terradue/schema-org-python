from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.educational_organization import EducationalOrganization


class CollegeOrUniversity(EducationalOrganization):
    """
A college, university, or other third-level educational institution.
    """
    type_: Literal['https://schema.org/CollegeOrUniversity'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CollegeOrUniversity'),serialization_alias='class') # type: ignore
