from typing import Literal
from pydantic import Field
from schemaorg_models.educational_organization import EducationalOrganization


class MiddleSchool(EducationalOrganization):
    """
A middle school (typically for children aged around 11-14, although this varies somewhat).
    """
    type_: Literal['https://schema.org/MiddleSchool'] = Field(default='https://schema.org/MiddleSchool', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
