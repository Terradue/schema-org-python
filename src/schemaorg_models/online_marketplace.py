from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.online_store import OnlineStore

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class OnlineMarketplace(OnlineStore):
    """
An eCommerce marketplace.
    """
    class_: Literal['https://schema.org/OnlineMarketplace'] = Field( # type: ignore
        default='https://schema.org/OnlineMarketplace',
        alias='@type',
        serialization_alias='@type'
    )
    hasStore: Optional[Union[OnlineStore, List[OnlineStore]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasStore',
            'https://schema.org/hasStore'
        ),
        serialization_alias='https://schema.org/hasStore'
    )
