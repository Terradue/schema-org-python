from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible


class AlignmentObject(Intangible):
    """
An intangible item that describes an alignment between a learning resource and a node in an educational framework.

Should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.
    """
    class_: Literal['https://schema.org/AlignmentObject'] = Field(default='https://schema.org/AlignmentObject', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    alignmentType: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('alignmentType', 'https://schema.org/alignmentType'), serialization_alias='https://schema.org/alignmentType')
    targetName: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('targetName', 'https://schema.org/targetName'), serialization_alias='https://schema.org/targetName')
    educationalFramework: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('educationalFramework', 'https://schema.org/educationalFramework'), serialization_alias='https://schema.org/educationalFramework')
    targetDescription: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('targetDescription', 'https://schema.org/targetDescription'), serialization_alias='https://schema.org/targetDescription')
    targetUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('targetUrl', 'https://schema.org/targetUrl'), serialization_alias='https://schema.org/targetUrl')
    @field_serializer('targetUrl')
    def targetUrl2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

