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
from .online_store import OnlineStore

class OnlineMarketplace(OnlineStore):
    '''
    An eCommerce marketplace.

    Attributes:
        hasStore: An eCommerce store part of an online marketplace.
    '''
    class_: Literal['https://schema.org/OnlineMarketplace'] = Field( # type: ignore
        default='https://schema.org/OnlineMarketplace',
        alias='@type',
        serialization_alias='@type'
    )
    hasStore: Optional[Union['OnlineStore', List['OnlineStore']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasStore',
            'https://schema.org/hasStore'
        ),
        serialization_alias='https://schema.org/hasStore'
    )
