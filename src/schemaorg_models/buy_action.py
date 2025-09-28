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
from .trade_action import TradeAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person
    from .warranty_promise import WarrantyPromise

class BuyAction(TradeAction):
    """
The act of giving money to a seller in exchange for goods or services rendered. An agent buys an object, product, or service from a seller for a price. Reciprocal of SellAction.
    """
    class_: Literal['https://schema.org/BuyAction'] = Field( # type: ignore
        default='https://schema.org/BuyAction',
        alias='@type',
        serialization_alias='@type'
    )
    seller: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seller',
            'https://schema.org/seller'
        ),
        serialization_alias='https://schema.org/seller'
    )
    vendor: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'vendor',
            'https://schema.org/vendor'
        ),
        serialization_alias='https://schema.org/vendor'
    )
    warrantyPromise: Optional[Union[WarrantyPromise, List[WarrantyPromise]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'warrantyPromise',
            'https://schema.org/warrantyPromise'
        ),
        serialization_alias='https://schema.org/warrantyPromise'
    )
