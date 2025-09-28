from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.defined_term_set import DefinedTermSet

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
from schemaorg_models.category_code import CategoryCode

class CategoryCodeSet(DefinedTermSet):
    """
A set of Category Code values.
    """
    class_: Literal['https://schema.org/CategoryCodeSet'] = Field( # type: ignore
        default='https://schema.org/CategoryCodeSet',
        alias='@type',
        serialization_alias='@type'
    )
    hasCategoryCode: Optional[Union[CategoryCode, List[CategoryCode]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCategoryCode',
            'https://schema.org/hasCategoryCode'
        ),
        serialization_alias='https://schema.org/hasCategoryCode'
    )
