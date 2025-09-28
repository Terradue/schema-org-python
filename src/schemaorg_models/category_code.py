from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .category_code_set import CategoryCodeSet
from .defined_term import DefinedTerm

class CategoryCode(DefinedTerm):
    """
A Category Code.
    """
    class_: Literal['https://schema.org/CategoryCode'] = Field( # type: ignore
        default='https://schema.org/CategoryCode',
        alias='@type',
        serialization_alias='@type'
    )
    inCodeSet: Optional[Union[HttpUrl, List[HttpUrl], CategoryCodeSet, List[CategoryCodeSet]]] = Field(
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
