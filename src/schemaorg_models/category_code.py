from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.defined_term import DefinedTerm

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

class CategoryCode(DefinedTerm):
    """
A Category Code.
    """
    class_: Literal['https://schema.org/CategoryCode'] = Field( # type: ignore
        default='https://schema.org/CategoryCode',
        alias='@type',
        serialization_alias='@type'
    )
    inCodeSet: Optional[Union[HttpUrl, List[HttpUrl], "CategoryCodeSet", List["CategoryCodeSet"]]] = Field(
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
