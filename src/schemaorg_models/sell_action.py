from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.trade_action import TradeAction

from schemaorg_models.person import Person
from schemaorg_models.organization import Organization
from schemaorg_models.warranty_promise import WarrantyPromise

class SellAction(TradeAction):
    """
The act of taking money from a buyer in exchange for goods or services rendered. An agent sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction.
    """
    class_: Literal['https://schema.org/SellAction'] = Field(default='https://schema.org/SellAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    buyer: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('buyer', 'https://schema.org/buyer'), serialization_alias='https://schema.org/buyer')
    warrantyPromise: Optional[Union[WarrantyPromise, List[WarrantyPromise]]] = Field(default=None, validation_alias=AliasChoices('warrantyPromise', 'https://schema.org/warrantyPromise'), serialization_alias='https://schema.org/warrantyPromise')
