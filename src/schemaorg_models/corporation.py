from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .organization import Organization

class Corporation(Organization):
    '''
    Organization: A business corporation.

    Attributes:
        tickerSymbol: The exchange traded instrument associated with a Corporation object. The tickerSymbol is expressed as an exchange and an instrument name separated by a space character. For the exchange component of the tickerSymbol attribute, we recommend using the controlled vocabulary of Market Identifier Codes (MIC) specified in ISO 15022.
    '''
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
