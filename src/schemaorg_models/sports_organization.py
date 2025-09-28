from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.organization import Organization

from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class SportsOrganization(Organization):
    """
Represents the collection of all sports organizations, including sports teams, governing bodies, and sports associations.
    """
    class_: Literal['https://schema.org/SportsOrganization'] = Field( # type: ignore
        default='https://schema.org/SportsOrganization',
        alias='@type',
        serialization_alias='@type'
    )
    sport: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sport',
            'https://schema.org/sport'
        ),
        serialization_alias='https://schema.org/sport'
    )
