from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.online_business import OnlineBusiness


class OnlineStore(OnlineBusiness):
    """
An eCommerce site.
    """
    type_: Literal['https://schema.org/OnlineStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OnlineStore'),serialization_alias='class') # type: ignore
    isStoreOn: Optional[Union["OnlineMarketplace", List["OnlineMarketplace"]]] = Field(default=None,validation_alias=AliasChoices('isStoreOn', 'https://schema.org/isStoreOn'),serialization_alias='https://schema.org/isStoreOn')
