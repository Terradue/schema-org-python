from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.online_store import OnlineStore

from schemaorg_models.online_store import OnlineStore

class OnlineMarketplace(OnlineStore):
    """
An eCommerce marketplace.
    """
    class_: Literal['https://schema.org/OnlineMarketplace'] = Field(default='https://schema.org/OnlineMarketplace', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    hasStore: Optional[Union[OnlineStore, List[OnlineStore]]] = Field(default=None, validation_alias=AliasChoices('hasStore', 'https://schema.org/hasStore'), serialization_alias='https://schema.org/hasStore')
