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
from .text import Text
from .language import Language

class PronounceableText(Text):
    """
Data type: PronounceableText.
    """
    class_: Literal['https://schema.org/PronounceableText'] = Field( # type: ignore
        default='https://schema.org/PronounceableText',
        alias='@type',
        serialization_alias='@type'
    )
    speechToTextMarkup: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'speechToTextMarkup',
            'https://schema.org/speechToTextMarkup'
        ),
        serialization_alias='https://schema.org/speechToTextMarkup'
    )
    inLanguage: Optional[Union[str, List[str], Language, List[Language]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inLanguage',
            'https://schema.org/inLanguage'
        ),
        serialization_alias='https://schema.org/inLanguage'
    )
    phoneticText: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'phoneticText',
            'https://schema.org/phoneticText'
        ),
        serialization_alias='https://schema.org/phoneticText'
    )
    textValue: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'textValue',
            'https://schema.org/textValue'
        ),
        serialization_alias='https://schema.org/textValue'
    )
