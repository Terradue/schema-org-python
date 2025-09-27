from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class Corporation(Organization):
    """
Organization: A business corporation.
    """
    type_: Literal['https://schema.org/Corporation'] = Field(default='https://schema.org/Corporation', alias='@type', serialization_alias='@type') # type: ignore
    tickerSymbol: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('tickerSymbol', 'https://schema.org/tickerSymbol'), serialization_alias='https://schema.org/tickerSymbol')
