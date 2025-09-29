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
from .scholarly_article import ScholarlyArticle

class MedicalScholarlyArticle(ScholarlyArticle):
    '''
    A scholarly article in the medical domain.

    Attributes:
        publicationType: The type of the medical article, taken from the US NLM MeSH publication type catalog. See also [MeSH documentation](http://www.nlm.nih.gov/mesh/pubtypes.html).
    '''
    class_: Literal['https://schema.org/MedicalScholarlyArticle'] = Field( # type: ignore
        default='https://schema.org/MedicalScholarlyArticle',
        alias='@type',
        serialization_alias='@type'
    )
    publicationType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
