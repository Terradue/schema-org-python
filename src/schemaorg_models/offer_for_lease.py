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

class OfferForLease(Offer):
    '''
    An [[OfferForLease]] in Schema.org represents an [[Offer]] to lease out something, i.e. an [[Offer]] whose
  [[businessFunction]] is [lease out](http://purl.org/goodrelations/v1#LeaseOut.). See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for
  background on the underlying concepts.
  
    '''
    class_: Literal['https://schema.org/OfferForLease'] = Field( # type: ignore
        default='https://schema.org/OfferForLease',
        alias='@type',
        serialization_alias='@type'
    )
