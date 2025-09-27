from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class Corporation(Organization):
    """
Organization: A business corporation.
    """
    type_: Literal['https://schema.org/Corporation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Corporation'),serialization_alias='class') # type: ignore
    tickerSymbol: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('tickerSymbol', 'https://schema.org/tickerSymbol'),serialization_alias='https://schema.org/tickerSymbol')
