from typing import Literal
from pydantic import Field
from schemaorg_models.educational_organization import EducationalOrganization


class School(EducationalOrganization):
    """
A school.
    """
    type_: Literal['https://schema.org/School'] = Field(default='https://schema.org/School', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
