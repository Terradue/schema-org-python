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
from .online_business import OnlineBusiness
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .online_marketplace import OnlineMarketplace

class OnlineStore(OnlineBusiness):
    '''
    An eCommerce site.

    Attributes:
        isStoreOn: The eCommerce marketplace this online store is on.
    '''
    class_: Literal['https://schema.org/OnlineStore'] = Field( # type: ignore
        default='https://schema.org/OnlineStore',
        alias='@type',
        serialization_alias='@type'
    )
    isStoreOn: Optional[Union['OnlineMarketplace', List['OnlineMarketplace']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
