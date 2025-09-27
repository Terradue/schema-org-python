from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.place import Place

from schemaorg_models.organization import Organization

class LocalBusiness(Place):
    """
A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.
    """
    type_: Literal['https://schema.org/LocalBusiness'] = Field(default='https://schema.org/LocalBusiness', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    paymentAccepted: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('paymentAccepted', 'https://schema.org/paymentAccepted'), serialization_alias='https://schema.org/paymentAccepted')
    priceRange: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('priceRange', 'https://schema.org/priceRange'), serialization_alias='https://schema.org/priceRange')
    branchOf: Optional[Union[Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('branchOf', 'https://schema.org/branchOf'), serialization_alias='https://schema.org/branchOf')
    currenciesAccepted: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('currenciesAccepted', 'https://schema.org/currenciesAccepted'), serialization_alias='https://schema.org/currenciesAccepted')
    openingHours: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('openingHours', 'https://schema.org/openingHours'), serialization_alias='https://schema.org/openingHours')
