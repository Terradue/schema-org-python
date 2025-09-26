from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.online_business import OnlineBusiness


class OnlineStore(OnlineBusiness):
    """
An eCommerce site.
    """
    isStoreOn: Optional[Union["OnlineMarketplace", List["OnlineMarketplace"]]] = Field(default=None,validation_alias=AliasChoices('isStoreOn', 'https://schema.org/isStoreOn'),serialization_alias='https://schema.org/isStoreOn')
