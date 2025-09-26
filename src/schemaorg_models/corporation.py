from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class Corporation(Organization):
    """
Organization: A business corporation.
    """
    tickerSymbol: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('tickerSymbol', 'https://schema.org/tickerSymbol'),serialization_alias='https://schema.org/tickerSymbol')
