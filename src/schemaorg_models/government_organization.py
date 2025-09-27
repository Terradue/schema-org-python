from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class GovernmentOrganization(Organization):
    """
A governmental organization or agency.
    """
    type_: Literal['https://schema.org/GovernmentOrganization'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GovernmentOrganization'),serialization_alias='class') # type: ignore
