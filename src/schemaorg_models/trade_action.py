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
from .action import Action
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .price_specification import PriceSpecification

class TradeAction(Action):
    """
The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.
    """
    class_: Literal['https://schema.org/TradeAction'] = Field( # type: ignore
        default='https://schema.org/TradeAction',
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
    priceSpecification: Optional[Union[PriceSpecification, List[PriceSpecification]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceSpecification',
            'https://schema.org/priceSpecification'
        ),
        serialization_alias='https://schema.org/priceSpecification'
    )
