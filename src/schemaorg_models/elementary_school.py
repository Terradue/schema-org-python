from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.educational_organization import EducationalOrganization


class ElementarySchool(EducationalOrganization):
    """
An elementary school.
    """
    type_: Literal['https://schema.org/ElementarySchool'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ElementarySchool'),serialization_alias='class') # type: ignore
