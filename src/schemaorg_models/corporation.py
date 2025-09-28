from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.organization import Organization

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

class Corporation(Organization):
    """
Organization: A business corporation.
    """
    class_: Literal['https://schema.org/Corporation'] = Field( # type: ignore
        default='https://schema.org/Corporation',
        alias='@type',
        serialization_alias='@type'
    )
    tickerSymbol: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tickerSymbol',
            'https://schema.org/tickerSymbol'
        ),
        serialization_alias='https://schema.org/tickerSymbol'
    )
