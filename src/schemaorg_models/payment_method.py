from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.intangible import Intangible

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

class PaymentMethod(Intangible):
    """
A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction. The following legacy values should be accepted:
    \
\
* http://purl.org/goodrelations/v1#ByBankTransferInAdvance\
* http://purl.org/goodrelations/v1#ByInvoice\
* http://purl.org/goodrelations/v1#Cash\
* http://purl.org/goodrelations/v1#CheckInAdvance\
* http://purl.org/goodrelations/v1#COD\
* http://purl.org/goodrelations/v1#DirectDebit\
* http://purl.org/goodrelations/v1#GoogleCheckout\
* http://purl.org/goodrelations/v1#PayPal\
* http://purl.org/goodrelations/v1#PaySwarm\
\
Structured values are recommended for newer payment methods.
    """
    class_: Literal['https://schema.org/PaymentMethod'] = Field( # type: ignore
        default='https://schema.org/PaymentMethod',
        alias='@type',
        serialization_alias='@type'
    )
    paymentMethodType: Optional[Union["PaymentMethodType", List["PaymentMethodType"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'paymentMethodType',
            'https://schema.org/paymentMethodType'
        ),
        serialization_alias='https://schema.org/paymentMethodType'
    )
