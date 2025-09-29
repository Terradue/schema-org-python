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
from .grant import Grant
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount
    from .organization import Organization
    from .person import Person

class MonetaryGrant(Grant):
    '''
    A monetary grant.

    Attributes:
        amount: The amount of money.
        funder: A person or organization that supports (sponsors) something through some kind of financial contribution.
    '''
    class_: Literal['https://schema.org/MonetaryGrant'] = Field( # type: ignore
        default='https://schema.org/MonetaryGrant',
        alias='@type',
        serialization_alias='@type'
    )
    amount: Optional[Union['MonetaryAmount', List['MonetaryAmount'], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amount',
            'https://schema.org/amount'
        ),
        serialization_alias='https://schema.org/amount'
    )
    funder: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funder',
            'https://schema.org/funder'
        ),
        serialization_alias='https://schema.org/funder'
    )
