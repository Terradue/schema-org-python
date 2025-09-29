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
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .language import Language

class PronounceableText(BaseModel):
    '''
    Data type: PronounceableText.

    Attributes:
        speechToTextMarkup: Form of markup used. eg. [SSML](https://www.w3.org/TR/speech-synthesis11) or [IPA](https://www.wikidata.org/wiki/Property:P898).
        inLanguage: The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
        phoneticText: Representation of a text [[textValue]] using the specified [[speechToTextMarkup]]. For example the city name of Houston in IPA: /ˈhjuːstən/.
        textValue: Text value being annotated.
    '''
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
    inLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
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
