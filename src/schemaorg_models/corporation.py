from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class Corporation(Organization):
    """
Organization: A business corporation.
    """
    class_: Literal['https://schema.org/Corporation'] = Field(default='https://schema.org/Corporation', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    tickerSymbol: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('tickerSymbol', 'https://schema.org/tickerSymbol'), serialization_alias='https://schema.org/tickerSymbol')
