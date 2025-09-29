from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
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
    '''
    Intended audience for an item, i.e. the group for whom the item was created.

    Attributes:
        geographicArea: The geographic area associated with the audience.
        audienceType: The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).
    '''
    class_: Literal['https://schema.org/Audience'] = Field( # type: ignore
        default='https://schema.org/Audience',
        alias='@type',
        serialization_alias='@type'
    )
    geographicArea: Optional[Union['AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    audienceType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
