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
from .defined_term_set import DefinedTermSet
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .category_code import CategoryCode

class CategoryCodeSet(DefinedTermSet):
    '''
    A set of Category Code values.

    Attributes:
        hasCategoryCode: A Category code contained in this code set.
    '''
    class_: Literal['https://schema.org/CategoryCodeSet'] = Field( # type: ignore
        default='https://schema.org/CategoryCodeSet',
        alias='@type',
        serialization_alias='@type'
    )
    hasCategoryCode: Optional[Union['CategoryCode', List['CategoryCode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
