from typing import Literal
from pydantic import Field
from schemaorg_models.educational_organization import EducationalOrganization


class School(EducationalOrganization):
    """
A school.
    """
    type_: Literal['https://schema.org/School'] = Field(default='https://schema.org/School', alias='@type', serialization_alias='@type') # type: ignore
