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
from .trade_action import TradeAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .warranty_promise import WarrantyPromise
    from .organization import Organization
    from .person import Person

class SellAction(TradeAction):
    '''
    The act of taking money from a buyer in exchange for goods or services rendered. An agent sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction.

    Attributes:
        buyer: A sub property of participant. The participant/person/organization that bought the object.
        warrantyPromise: The warranty promise(s) included in the offer.
    '''
    class_: Literal['https://schema.org/SellAction'] = Field( # type: ignore
        default='https://schema.org/SellAction',
        alias='@type',
        serialization_alias='@type'
    )
    buyer: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    warrantyPromise: Optional[Union['WarrantyPromise', List['WarrantyPromise']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
