from typing import Literal
from pydantic import Field
from schemaorg_models.educational_organization import EducationalOrganization


class HighSchool(EducationalOrganization):
    """
A high school.
    """
    class_: Literal['https://schema.org/HighSchool'] = Field('class', alias='class', serialization_alias='class') # type: ignore
