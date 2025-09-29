from __future__ import annotations
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
from .transfer_action import TransferAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .contact_point import ContactPoint
    from .price_specification import PriceSpecification
    from .person import Person
    from .organization import Organization
    from .audience import Audience

class DonateAction(TransferAction):
    """
The act of providing goods, services, or money without compensation, often for philanthropic reasons.
    """
    class_: Literal['https://schema.org/DonateAction'] = Field( # type: ignore
        default='https://schema.org/DonateAction',
        alias='@type',
        serialization_alias='@type'
    )
    price: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'price',
            'https://schema.org/price'
        ),
        serialization_alias='https://schema.org/price'
    )
    priceCurrency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceCurrency',
            'https://schema.org/priceCurrency'
        ),
        serialization_alias='https://schema.org/priceCurrency'
    )
    priceSpecification: Optional[Union["PriceSpecification", List["PriceSpecification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceSpecification',
            'https://schema.org/priceSpecification'
        ),
        serialization_alias='https://schema.org/priceSpecification'
    )
    recipient: Optional[Union["Organization", List["Organization"], "Audience", List["Audience"], "ContactPoint", List["ContactPoint"], "Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipient',
            'https://schema.org/recipient'
        ),
        serialization_alias='https://schema.org/recipient'
    )
