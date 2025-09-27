from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class GovernmentOrganization(Organization):
    """
A governmental organization or agency.
    """
    type_: Literal['https://schema.org/GovernmentOrganization'] = Field(default='https://schema.org/GovernmentOrganization', alias='@type', serialization_alias='@type') # type: ignore
