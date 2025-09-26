from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class MovieTheater(CivicStructure):
    """
A movie theater.
    """
    screenCount: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('screenCount', 'https://schema.org/screenCount'),serialization_alias='https://schema.org/screenCount')
