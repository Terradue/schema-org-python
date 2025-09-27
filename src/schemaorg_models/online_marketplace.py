from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.online_store import OnlineStore

from schemaorg_models.online_store import OnlineStore

class OnlineMarketplace(OnlineStore):
    """
An eCommerce marketplace.
    """
    type_: Literal['https://schema.org/OnlineMarketplace'] = Field(default='https://schema.org/OnlineMarketplace', alias='@type', serialization_alias='@type') # type: ignore
    hasStore: Optional[Union[OnlineStore, List[OnlineStore]]] = Field(default=None, validation_alias=AliasChoices('hasStore', 'https://schema.org/hasStore'), serialization_alias='https://schema.org/hasStore')
