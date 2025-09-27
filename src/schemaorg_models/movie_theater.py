from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class MovieTheater(CivicStructure):
    """
A movie theater.
    """
    type_: Literal['https://schema.org/MovieTheater'] = Field(default='https://schema.org/MovieTheater', alias='@type', serialization_alias='@type') # type: ignore
    screenCount: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('screenCount', 'https://schema.org/screenCount'), serialization_alias='https://schema.org/screenCount')
