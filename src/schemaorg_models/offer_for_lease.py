from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.offer import Offer


class OfferForLease(Offer):
    """
An [[OfferForLease]] in Schema.org represents an [[Offer]] to lease out something, i.e. an [[Offer]] whose
  [[businessFunction]] is [lease out](http://purl.org/goodrelations/v1#LeaseOut.). See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for
  background on the underlying concepts.
  
    """
    type_: Literal['https://schema.org/OfferForLease'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OfferForLease'),serialization_alias='class') # type: ignore
