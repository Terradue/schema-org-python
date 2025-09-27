from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.defined_term_set import DefinedTermSet

from schemaorg_models.category_code import CategoryCode

class CategoryCodeSet(DefinedTermSet):
    """
A set of Category Code values.
    """
    class_: Literal['https://schema.org/CategoryCodeSet'] = Field(default='https://schema.org/CategoryCodeSet', alias='class', serialization_alias='class') # type: ignore
    hasCategoryCode: Optional[Union[CategoryCode, List[CategoryCode]]] = Field(default=None, validation_alias=AliasChoices('hasCategoryCode', 'https://schema.org/hasCategoryCode'), serialization_alias='https://schema.org/hasCategoryCode')
