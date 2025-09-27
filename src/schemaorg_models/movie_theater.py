from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class MovieTheater(CivicStructure):
    """
A movie theater.
    """
    class_: Literal['https://schema.org/MovieTheater'] = Field(default='https://schema.org/MovieTheater', alias='class', serialization_alias='class') # type: ignore
    screenCount: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('screenCount', 'https://schema.org/screenCount'), serialization_alias='https://schema.org/screenCount')
