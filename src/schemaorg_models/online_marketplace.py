from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.online_store import OnlineStore

from schemaorg_models.online_store import OnlineStore

class OnlineMarketplace(OnlineStore):
    """
An eCommerce marketplace.
    """
    type_: Literal['https://schema.org/OnlineMarketplace'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OnlineMarketplace'),serialization_alias='class') # type: ignore
    hasStore: Optional[Union[OnlineStore, List[OnlineStore]]] = Field(default=None,validation_alias=AliasChoices('hasStore', 'https://schema.org/hasStore'),serialization_alias='https://schema.org/hasStore')
