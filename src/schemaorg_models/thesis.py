from __future__ import annotations
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
from .creative_work import CreativeWork

class Thesis(CreativeWork):
    """
A thesis or dissertation document submitted in support of candidature for an academic degree or professional qualification.
    """
    class_: Literal['https://schema.org/Thesis'] = Field( # type: ignore
        default='https://schema.org/Thesis',
        alias='@type',
        serialization_alias='@type'
    )
    inSupportOf: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inSupportOf',
            'https://schema.org/inSupportOf'
        ),
        serialization_alias='https://schema.org/inSupportOf'
    )
