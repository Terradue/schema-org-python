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
from .creative_work import CreativeWork

class PublicationVolume(CreativeWork):
    '''
    A part of a successively published publication such as a periodical or multi-volume work, often numbered. It may represent a time span, such as a year.\
\
See also [blog post](https://blog-schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).

    Attributes:
        pagination: Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".
        pageStart: The page on which the work starts; for example "135" or "xiii".
        pageEnd: The page on which the work ends; for example "138" or "xvi".
        volumeNumber: Identifies the volume of publication or multi-part work; for example, "iii" or "2".
    '''
    class_: Literal['https://schema.org/PublicationVolume'] = Field( # type: ignore
        default='https://schema.org/PublicationVolume',
        alias='@type',
        serialization_alias='@type'
    )
    pagination: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pagination',
            'https://schema.org/pagination'
        ),
        serialization_alias='https://schema.org/pagination'
    )
    pageStart: Optional[Union[int, List[int], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pageStart',
            'https://schema.org/pageStart'
        ),
        serialization_alias='https://schema.org/pageStart'
    )
    pageEnd: Optional[Union[str, List[str], int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pageEnd',
            'https://schema.org/pageEnd'
        ),
        serialization_alias='https://schema.org/pageEnd'
    )
    volumeNumber: Optional[Union[str, List[str], int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'volumeNumber',
            'https://schema.org/volumeNumber'
        ),
        serialization_alias='https://schema.org/volumeNumber'
    )
