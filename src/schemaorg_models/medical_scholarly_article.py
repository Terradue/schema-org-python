from __future__ import annotations

from .scholarly_article import ScholarlyArticle    

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

class MedicalScholarlyArticle(ScholarlyArticle):
    """
A scholarly article in the medical domain.
    """
    class_: Literal['https://schema.org/MedicalScholarlyArticle'] = Field( # type: ignore
        default='https://schema.org/MedicalScholarlyArticle',
        alias='@type',
        serialization_alias='@type'
    )
    publicationType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publicationType',
            'https://schema.org/publicationType'
        ),
        serialization_alias='https://schema.org/publicationType'
    )
