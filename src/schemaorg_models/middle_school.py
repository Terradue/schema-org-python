from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.educational_organization import EducationalOrganization


class MiddleSchool(EducationalOrganization):
    """
A middle school (typically for children aged around 11-14, although this varies somewhat).
    """
    type_: Literal['https://schema.org/MiddleSchool'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MiddleSchool'),serialization_alias='class') # type: ignore
