from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class GovernmentOrganization(Organization):
    """
A governmental organization or agency.
    """
    class_: Literal['https://schema.org/GovernmentOrganization'] = Field('class', alias='class', serialization_alias='class') # type: ignore
