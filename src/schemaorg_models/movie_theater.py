from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class MovieTheater(CivicStructure):
    """
A movie theater.
    """
    type_: Literal['https://schema.org/MovieTheater'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MovieTheater'),serialization_alias='class') # type: ignore
    screenCount: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('screenCount', 'https://schema.org/screenCount'),serialization_alias='https://schema.org/screenCount')
