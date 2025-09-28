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
    from .person import Person
    from .organization import Organization
    from .real_estate_agent import RealEstateAgent

class RentAction(TradeAction):
    """
The act of giving money in return for temporary use, but not ownership, of an object such as a vehicle or property. For example, an agent rents a property from a landlord in exchange for a periodic payment.
    """
    class_: Literal['https://schema.org/RentAction'] = Field( # type: ignore
        default='https://schema.org/RentAction',
        alias='@type',
        serialization_alias='@type'
    )
    realEstateAgent: Optional[Union[RealEstateAgent, List[RealEstateAgent]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'realEstateAgent',
            'https://schema.org/realEstateAgent'
        ),
        serialization_alias='https://schema.org/realEstateAgent'
    )
    landlord: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'landlord',
            'https://schema.org/landlord'
        ),
        serialization_alias='https://schema.org/landlord'
    )
