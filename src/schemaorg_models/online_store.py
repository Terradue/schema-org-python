from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.online_business import OnlineBusiness


class OnlineStore(OnlineBusiness):
    """
An eCommerce site.
    """
    class_: Literal['https://schema.org/OnlineStore'] = Field(default='https://schema.org/OnlineStore', alias='@type', serialization_alias='@type') # type: ignore
    isStoreOn: Optional[Union["OnlineMarketplace", List["OnlineMarketplace"]]] = Field(default=None, validation_alias=AliasChoices('isStoreOn', 'https://schema.org/isStoreOn'), serialization_alias='https://schema.org/isStoreOn')
