from __future__ import annotations
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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea

class Audience(Intangible):
    """
Intended audience for an item, i.e. the group for whom the item was created.
    """
    class_: Literal['https://schema.org/Audience'] = Field( # type: ignore
        default='https://schema.org/Audience',
        alias='@type',
        serialization_alias='@type'
    )
    geographicArea: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geographicArea',
            'https://schema.org/geographicArea'
        ),
        serialization_alias='https://schema.org/geographicArea'
    )
    audienceType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'audienceType',
            'https://schema.org/audienceType'
        ),
        serialization_alias='https://schema.org/audienceType'
    )
