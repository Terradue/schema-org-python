from typing import Literal
from pydantic import Field
from schemaorg_models.offer import Offer


class OfferForPurchase(Offer):
    """
An [[OfferForPurchase]] in Schema.org represents an [[Offer]] to sell something, i.e. an [[Offer]] whose
  [[businessFunction]] is [sell](http://purl.org/goodrelations/v1#Sell.). See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for
  background on the underlying concepts.
  
    """
    class_: Literal['https://schema.org/OfferForPurchase'] = Field(default='https://schema.org/OfferForPurchase', alias='class', serialization_alias='class') # type: ignore
