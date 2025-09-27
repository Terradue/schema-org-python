from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class ResearchOrganization(Organization):
    """
A Research Organization (e.g. scientific institute, research company).
    """
    class_: Literal['https://schema.org/ResearchOrganization'] = Field(default='https://schema.org/ResearchOrganization', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
