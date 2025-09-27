from typing import Literal
from pydantic import Field
from schemaorg_models.offer import Offer


class OfferForLease(Offer):
    """
An [[OfferForLease]] in Schema.org represents an [[Offer]] to lease out something, i.e. an [[Offer]] whose
  [[businessFunction]] is [lease out](http://purl.org/goodrelations/v1#LeaseOut.). See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for
  background on the underlying concepts.
  
    """
    class_: Literal['https://schema.org/OfferForLease'] = Field(default='https://schema.org/OfferForLease', alias='@type', serialization_alias='@type') # type: ignore
