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
from .defined_term import DefinedTerm
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .category_code_set import CategoryCodeSet

class CategoryCode(DefinedTerm):
    '''
    A Category Code.

    Attributes:
        inCodeSet: A [[CategoryCodeSet]] that contains this category code.
        codeValue: A short textual code that uniquely identifies the value.
    '''
    class_: Literal['https://schema.org/CategoryCode'] = Field( # type: ignore
        default='https://schema.org/CategoryCode',
        alias='@type',
        serialization_alias='@type'
    )
    inCodeSet: Optional[Union[HttpUrl, List[HttpUrl], 'CategoryCodeSet', List['CategoryCodeSet']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inCodeSet',
            'https://schema.org/inCodeSet'
        ),
        serialization_alias='https://schema.org/inCodeSet'
    )
    codeValue: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'codeValue',
            'https://schema.org/codeValue'
        ),
        serialization_alias='https://schema.org/codeValue'
    )
