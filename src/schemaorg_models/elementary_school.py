from typing import Literal
from pydantic import Field
from schemaorg_models.educational_organization import EducationalOrganization


class ElementarySchool(EducationalOrganization):
    """
An elementary school.
    """
    type_: Literal['https://schema.org/ElementarySchool'] = Field(default='https://schema.org/ElementarySchool', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
