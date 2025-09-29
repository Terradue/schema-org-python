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
    from .organization import Organization
    from .real_estate_agent import RealEstateAgent
    from .person import Person

class RentAction(TradeAction):
    '''
    The act of giving money in return for temporary use, but not ownership, of an object such as a vehicle or property. For example, an agent rents a property from a landlord in exchange for a periodic payment.

    Attributes:
        realEstateAgent: A sub property of participant. The real estate agent involved in the action.
        landlord: A sub property of participant. The owner of the real estate property.
    '''
    class_: Literal['https://schema.org/RentAction'] = Field( # type: ignore
        default='https://schema.org/RentAction',
        alias='@type',
        serialization_alias='@type'
    )
    realEstateAgent: Optional[Union['RealEstateAgent', List['RealEstateAgent']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    landlord: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
