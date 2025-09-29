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
from .offer import Offer

class OfferForPurchase(Offer):
    '''
    An [[OfferForPurchase]] in Schema.org represents an [[Offer]] to sell something, i.e. an [[Offer]] whose
  [[businessFunction]] is [sell](http://purl.org/goodrelations/v1#Sell.). See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for
  background on the underlying concepts.
  
    '''
    class_: Literal['https://schema.org/OfferForPurchase'] = Field( # type: ignore
        default='https://schema.org/OfferForPurchase',
        alias='@type',
        serialization_alias='@type'
    )
