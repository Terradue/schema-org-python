from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.defined_term import DefinedTerm


class CategoryCode(DefinedTerm):
    """
A Category Code.
    """
    inCodeSet: Optional[Union[HttpUrl, List[HttpUrl], "CategoryCodeSet", List["CategoryCodeSet"]]] = Field(default=None,validation_alias=AliasChoices('inCodeSet', 'https://schema.org/inCodeSet'),serialization_alias='https://schema.org/inCodeSet')
    @field_serializer('inCodeSet')
    def inCodeSet2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    codeValue: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('codeValue', 'https://schema.org/codeValue'),serialization_alias='https://schema.org/codeValue')
