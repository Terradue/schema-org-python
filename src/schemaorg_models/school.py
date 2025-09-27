from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.educational_organization import EducationalOrganization


class School(EducationalOrganization):
    """
A school.
    """
    type_: Literal['https://schema.org/School'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/School'),serialization_alias='class') # type: ignore
