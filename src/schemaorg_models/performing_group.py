from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class PerformingGroup(Organization):
    """
A performance group, such as a band, an orchestra, or a circus.
    """
    type_: Literal['https://schema.org/PerformingGroup'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PerformingGroup'),serialization_alias='class') # type: ignore
