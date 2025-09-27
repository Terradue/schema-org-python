from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class GovernmentOrganization(Organization):
    """
A governmental organization or agency.
    """
    class_: Literal['https://schema.org/GovernmentOrganization'] = Field(default='https://schema.org/GovernmentOrganization', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
