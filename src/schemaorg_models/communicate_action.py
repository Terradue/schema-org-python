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
from .interact_action import InteractAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .thing import Thing
    from .audience import Audience
    from .organization import Organization
    from .language import Language
    from .person import Person
    from .contact_point import ContactPoint

class CommunicateAction(InteractAction):
    '''
    The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.

    Attributes:
        inLanguage: The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
        about: The subject matter of the content.
        recipient: A sub property of participant. The participant who is at the receiving end of the action.
        language: A sub property of instrument. The language used on this action.
    '''
    class_: Literal['https://schema.org/CommunicateAction'] = Field( # type: ignore
        default='https://schema.org/CommunicateAction',
        alias='@type',
        serialization_alias='@type'
    )
    inLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inLanguage',
            'https://schema.org/inLanguage'
        ),
        serialization_alias='https://schema.org/inLanguage'
    )
    about: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'about',
            'https://schema.org/about'
        ),
        serialization_alias='https://schema.org/about'
    )
    recipient: Optional[Union['Organization', List['Organization'], 'Audience', List['Audience'], 'ContactPoint', List['ContactPoint'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipient',
            'https://schema.org/recipient'
        ),
        serialization_alias='https://schema.org/recipient'
    )
    language: Optional[Union['Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'language',
            'https://schema.org/language'
        ),
        serialization_alias='https://schema.org/language'
    )
