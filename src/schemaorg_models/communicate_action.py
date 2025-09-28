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
from .contact_point import ContactPoint
from .language import Language
from .person import Person
from .thing import Thing
from .interact_action import InteractAction
from .organization import Organization
from .audience import Audience

class CommunicateAction(InteractAction):
    """
The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.
    """
    class_: Literal['https://schema.org/CommunicateAction'] = Field( # type: ignore
        default='https://schema.org/CommunicateAction',
        alias='@type',
        serialization_alias='@type'
    )
    inLanguage: Optional[Union[str, List[str], Language, List[Language]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inLanguage',
            'https://schema.org/inLanguage'
        ),
        serialization_alias='https://schema.org/inLanguage'
    )
    about: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'about',
            'https://schema.org/about'
        ),
        serialization_alias='https://schema.org/about'
    )
    recipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], ContactPoint, List[ContactPoint], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipient',
            'https://schema.org/recipient'
        ),
        serialization_alias='https://schema.org/recipient'
    )
    language: Optional[Union[Language, List[Language]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'language',
            'https://schema.org/language'
        ),
        serialization_alias='https://schema.org/language'
    )
