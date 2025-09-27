from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.defined_term import DefinedTerm


class CategoryCode(DefinedTerm):
    """
A Category Code.
    """
    class_: Literal['https://schema.org/CategoryCode'] = Field(default='https://schema.org/CategoryCode', alias='@type', serialization_alias='@type') # type: ignore
    inCodeSet: Optional[Union[HttpUrl, List[HttpUrl], "CategoryCodeSet", List["CategoryCodeSet"]]] = Field(default=None, validation_alias=AliasChoices('inCodeSet', 'https://schema.org/inCodeSet'), serialization_alias='https://schema.org/inCodeSet')
    @field_serializer('inCodeSet')
    def inCodeSet2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    codeValue: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('codeValue', 'https://schema.org/codeValue'), serialization_alias='https://schema.org/codeValue')
