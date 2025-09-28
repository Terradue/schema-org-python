from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.payment_card import PaymentCard

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CreditCard(PaymentCard):
    """
A card payment method of a particular brand or name.  Used to mark up a particular payment method and/or the financial product/service that supplies the card account.\
\
Commonly used values:\
\
* http://purl.org/goodrelations/v1#AmericanExpress\
* http://purl.org/goodrelations/v1#DinersClub\
* http://purl.org/goodrelations/v1#Discover\
* http://purl.org/goodrelations/v1#JCB\
* http://purl.org/goodrelations/v1#MasterCard\
* http://purl.org/goodrelations/v1#VISA
       
    """
    class_: Literal['https://schema.org/CreditCard'] = Field( # type: ignore
        default='https://schema.org/CreditCard',
        alias='@type',
        serialization_alias='@type'
    )
