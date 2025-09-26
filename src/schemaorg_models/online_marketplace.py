from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.online_store import OnlineStore

from schemaorg_models.online_store import OnlineStore

class OnlineMarketplace(OnlineStore):
    """
An eCommerce marketplace.
    """
    hasStore: Optional[Union[OnlineStore, List[OnlineStore]]] = Field(default=None,validation_alias=AliasChoices('hasStore', 'https://schema.org/hasStore'),serialization_alias='https://schema.org/hasStore')
