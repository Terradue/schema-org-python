from typing import Literal
from pydantic import Field
from schemaorg_models.educational_organization import EducationalOrganization


class Preschool(EducationalOrganization):
    """
A preschool.
    """
    type_: Literal['https://schema.org/Preschool'] = Field(default='https://schema.org/Preschool', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
