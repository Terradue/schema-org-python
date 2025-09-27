from typing import Literal
from pydantic import Field
from schemaorg_models.educational_organization import EducationalOrganization


class ElementarySchool(EducationalOrganization):
    """
An elementary school.
    """
    class_: Literal['https://schema.org/ElementarySchool'] = Field(default='https://schema.org/ElementarySchool', alias='@type', serialization_alias='@type') # type: ignore
