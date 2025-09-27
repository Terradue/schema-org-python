from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class TradeAction(Action):
    """
The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.
    """
    type_: Literal['https://schema.org/TradeAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TradeAction'),serialization_alias='class') # type: ignore
    price: Optional[Union[str, List[str], float, List[float]]] = Field(default=None,validation_alias=AliasChoices('price', 'https://schema.org/price'),serialization_alias='https://schema.org/price')
    priceCurrency: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('priceCurrency', 'https://schema.org/priceCurrency'),serialization_alias='https://schema.org/priceCurrency')
    priceSpecification: Optional[Union["PriceSpecification", List["PriceSpecification"]]] = Field(default=None,validation_alias=AliasChoices('priceSpecification', 'https://schema.org/priceSpecification'),serialization_alias='https://schema.org/priceSpecification')
