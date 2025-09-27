from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.event import Event


class EducationEvent(Event):
    """
Event type: Education event.
    """
    class_: Literal['https://schema.org/EducationEvent'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    educationalLevel: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(default=None,validation_alias=AliasChoices('educationalLevel', 'https://schema.org/educationalLevel'), serialization_alias='https://schema.org/educationalLevel')
    @field_serializer('educationalLevel')
    def educationalLevel2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    assesses: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('assesses', 'https://schema.org/assesses'), serialization_alias='https://schema.org/assesses')
    teaches: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('teaches', 'https://schema.org/teaches'), serialization_alias='https://schema.org/teaches')
