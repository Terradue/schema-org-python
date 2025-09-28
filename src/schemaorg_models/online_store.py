from __future__ import annotations

from .online_business import OnlineBusiness    

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

class OnlineStore(OnlineBusiness):
    """
An eCommerce site.
    """
    class_: Literal['https://schema.org/OnlineStore'] = Field( # type: ignore
        default='https://schema.org/OnlineStore',
        alias='@type',
        serialization_alias='@type'
    )
    isStoreOn: Optional[Union["OnlineMarketplace", List["OnlineMarketplace"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isStoreOn',
            'https://schema.org/isStoreOn'
        ),
        serialization_alias='https://schema.org/isStoreOn'
    )
