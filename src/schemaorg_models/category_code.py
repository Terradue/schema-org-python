from typing import Union, List, Optional
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.defined_term import DefinedTerm


class CategoryCode(DefinedTerm):
    """
A Category Code.
    """
    inCodeSet: Optional[Union[HttpUrl, List[HttpUrl], "CategoryCodeSet", List["CategoryCodeSet"]]] = Field(default=None,validation_alias=AliasChoices('inCodeSet', 'https://schema.org/inCodeSet'),serialization_alias='https://schema.org/inCodeSet')
    codeValue: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('codeValue', 'https://schema.org/codeValue'),serialization_alias='https://schema.org/codeValue')
