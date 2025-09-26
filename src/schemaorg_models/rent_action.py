from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.trade_action import TradeAction

from schemaorg_models.real_estate_agent import RealEstateAgent
from schemaorg_models.organization import Organization
from schemaorg_models.person import Person

class RentAction(TradeAction):
    """
The act of giving money in return for temporary use, but not ownership, of an object such as a vehicle or property. For example, an agent rents a property from a landlord in exchange for a periodic payment.
    """
    realEstateAgent: Optional[Union[RealEstateAgent, List[RealEstateAgent]]] = Field(default=None,validation_alias=AliasChoices('realEstateAgent', 'https://schema.org/realEstateAgent'),serialization_alias='https://schema.org/realEstateAgent')
    landlord: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('landlord', 'https://schema.org/landlord'),serialization_alias='https://schema.org/landlord')
