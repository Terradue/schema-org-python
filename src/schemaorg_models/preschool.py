from typing import Literal
from pydantic import Field
from schemaorg_models.educational_organization import EducationalOrganization


class Preschool(EducationalOrganization):
    """
A preschool.
    """
    class_: Literal['https://schema.org/Preschool'] = Field(default='https://schema.org/Preschool', alias='class', serialization_alias='class') # type: ignore
