from __future__ import annotations

from .role import Role    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class OrganizationRole(Role):
    """
A subclass of Role used to describe roles within organizations.
    """
    class_: Literal['https://schema.org/OrganizationRole'] = Field( # type: ignore
        default='https://schema.org/OrganizationRole',
        alias='@type',
        serialization_alias='@type'
    )
    numberedPosition: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberedPosition',
            'https://schema.org/numberedPosition'
        ),
        serialization_alias='https://schema.org/numberedPosition'
    )
