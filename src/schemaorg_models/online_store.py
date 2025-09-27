from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.online_business import OnlineBusiness


class OnlineStore(OnlineBusiness):
    """
An eCommerce site.
    """
    type_: Literal['https://schema.org/OnlineStore'] = Field(default='https://schema.org/OnlineStore', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    isStoreOn: Optional[Union["OnlineMarketplace", List["OnlineMarketplace"]]] = Field(default=None, validation_alias=AliasChoices('isStoreOn', 'https://schema.org/isStoreOn'), serialization_alias='https://schema.org/isStoreOn')
