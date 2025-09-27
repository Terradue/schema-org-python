from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.educational_organization import EducationalOrganization


class HighSchool(EducationalOrganization):
    """
A high school.
    """
    type_: Literal['https://schema.org/HighSchool'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HighSchool'),serialization_alias='class') # type: ignore
