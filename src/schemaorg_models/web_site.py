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

class WebSite(CreativeWork):
    '''
    A WebSite is a set of related web pages and other items typically served from a single web domain and accessible via URLs.

    Attributes:
        issn: The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication.
    '''
    class_: Literal['https://schema.org/WebSite'] = Field( # type: ignore
        default='https://schema.org/WebSite',
        alias='@type',
        serialization_alias='@type'
    )
    issn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'issn',
            'https://schema.org/issn'
        ),
        serialization_alias='https://schema.org/issn'
    )
