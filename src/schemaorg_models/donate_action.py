from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.transfer_action import TransferAction

from schemaorg_models.price_specification import PriceSpecification
from schemaorg_models.organization import Organization
from schemaorg_models.audience import Audience
from schemaorg_models.contact_point import ContactPoint
from schemaorg_models.person import Person

class DonateAction(TransferAction):
    """
The act of providing goods, services, or money without compensation, often for philanthropic reasons.
    """
    type_: Literal['https://schema.org/DonateAction'] = Field(default='https://schema.org/DonateAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    price: Optional[Union[str, List[str], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('price', 'https://schema.org/price'), serialization_alias='https://schema.org/price')
    priceCurrency: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('priceCurrency', 'https://schema.org/priceCurrency'), serialization_alias='https://schema.org/priceCurrency')
    priceSpecification: Optional[Union[PriceSpecification, List[PriceSpecification]]] = Field(default=None, validation_alias=AliasChoices('priceSpecification', 'https://schema.org/priceSpecification'), serialization_alias='https://schema.org/priceSpecification')
    recipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], ContactPoint, List[ContactPoint], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('recipient', 'https://schema.org/recipient'), serialization_alias='https://schema.org/recipient')
