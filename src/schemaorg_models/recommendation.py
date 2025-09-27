from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.review import Review

from schemaorg_models.physical_activity_category import PhysicalActivityCategory
from schemaorg_models.category_code import CategoryCode
from schemaorg_models.thing import Thing

class Recommendation(Review):
    """
[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the best option or best course of action. Recommendations may be for products or services, or other concrete things, as in the case of a ranked list or product guide. A [[Guide]] may list multiple recommendations for different categories. For example, in a [[Guide]] about which TVs to buy, the author may have several [[Recommendation]]s.
    """
    type_: Literal['https://schema.org/Recommendation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Recommendation'),serialization_alias='class') # type: ignore
    category: Optional[Union[PhysicalActivityCategory, List[PhysicalActivityCategory], CategoryCode, List[CategoryCode], str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('category', 'https://schema.org/category'),serialization_alias='https://schema.org/category')
    @field_serializer('category')
    def category2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

