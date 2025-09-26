from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.event import Event


class EducationEvent(Event):
    """
Event type: Education event.
    """
    educationalLevel: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(default=None,validation_alias=AliasChoices('educationalLevel', 'https://schema.org/educationalLevel'),serialization_alias='https://schema.org/educationalLevel')
    @field_serializer('educationalLevel')
    def educationalLevel2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    assesses: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('assesses', 'https://schema.org/assesses'),serialization_alias='https://schema.org/assesses')
    teaches: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('teaches', 'https://schema.org/teaches'),serialization_alias='https://schema.org/teaches')
