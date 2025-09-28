from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.civic_structure import CivicStructure

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

class MovieTheater(CivicStructure):
    """
A movie theater.
    """
    class_: Literal['https://schema.org/MovieTheater'] = Field( # type: ignore
        default='https://schema.org/MovieTheater',
        alias='@type',
        serialization_alias='@type'
    )
    screenCount: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'screenCount',
            'https://schema.org/screenCount'
        ),
        serialization_alias='https://schema.org/screenCount'
    )
