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
from .create_action import CreateAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .language import Language

class WriteAction(CreateAction):
    '''
    The act of authoring written creative content.

    Attributes:
        language: A sub property of instrument. The language used on this action.
        inLanguage: The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
    '''
    class_: Literal['https://schema.org/WriteAction'] = Field( # type: ignore
        default='https://schema.org/WriteAction',
        alias='@type',
        serialization_alias='@type'
    )
    language: Optional[Union['Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'language',
            'https://schema.org/language'
        ),
        serialization_alias='https://schema.org/language'
    )
    inLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inLanguage',
            'https://schema.org/inLanguage'
        ),
        serialization_alias='https://schema.org/inLanguage'
    )
