from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.educational_organization import EducationalOrganization


class Preschool(EducationalOrganization):
    """
A preschool.
    """
    type_: Literal['https://schema.org/Preschool'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Preschool'),serialization_alias='class') # type: ignore
