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
from .review import Review
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .category_code import CategoryCode
    from .thing import Thing
    from .physical_activity_category import PhysicalActivityCategory

class Recommendation(Review):
    """
[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the best option or best course of action. Recommendations may be for products or services, or other concrete things, as in the case of a ranked list or product guide. A [[Guide]] may list multiple recommendations for different categories. For example, in a [[Guide]] about which TVs to buy, the author may have several [[Recommendation]]s.
    """
    class_: Literal['https://schema.org/Recommendation'] = Field( # type: ignore
        default='https://schema.org/Recommendation',
        alias='@type',
        serialization_alias='@type'
    )
    category: Optional[Union["PhysicalActivityCategory", List["PhysicalActivityCategory"], "CategoryCode", List["CategoryCode"], str, List[str], "Thing", List["Thing"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'category',
            'https://schema.org/category'
        ),
        serialization_alias='https://schema.org/category'
    )
