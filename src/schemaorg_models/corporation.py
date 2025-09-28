from __future__ import annotations
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
from .organization import Organization

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
