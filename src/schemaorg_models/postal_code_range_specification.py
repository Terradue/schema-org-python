from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .structured_value import StructuredValue

class PostalCodeRangeSpecification(StructuredValue):
    '''
    Indicates a range of postal codes, usually defined as the set of valid codes between [[postalCodeBegin]] and [[postalCodeEnd]], inclusively.

    Attributes:
        postalCodeBegin: First postal code in a range (included).
        postalCodeEnd: Last postal code in the range (included). Needs to be after [[postalCodeBegin]].
    '''
    class_: Literal['https://schema.org/PostalCodeRangeSpecification'] = Field( # type: ignore
        default='https://schema.org/PostalCodeRangeSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    postalCodeBegin: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postalCodeBegin',
            'https://schema.org/postalCodeBegin'
        ),
        serialization_alias='https://schema.org/postalCodeBegin'
    )
    postalCodeEnd: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postalCodeEnd',
            'https://schema.org/postalCodeEnd'
        ),
        serialization_alias='https://schema.org/postalCodeEnd'
    )
