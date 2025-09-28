from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.creative_work import CreativeWork

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class PublicationVolume(CreativeWork):
    """
A part of a successively published publication such as a periodical or multi-volume work, often numbered. It may represent a time span, such as a year.\
\
See also [blog post](https://blog-schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).
    """
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
