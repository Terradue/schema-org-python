from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.interact_action import InteractAction

from schemaorg_models.language import Language
from schemaorg_models.thing import Thing
from schemaorg_models.organization import Organization
from schemaorg_models.audience import Audience
from schemaorg_models.contact_point import ContactPoint
from schemaorg_models.person import Person

class CommunicateAction(InteractAction):
    """
The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.
    """
    class_: Literal['https://schema.org/CommunicateAction'] = Field(default='https://schema.org/CommunicateAction', alias='class', serialization_alias='class') # type: ignore
    inLanguage: Optional[Union[str, List[str], Language, List[Language]]] = Field(default=None, validation_alias=AliasChoices('inLanguage', 'https://schema.org/inLanguage'), serialization_alias='https://schema.org/inLanguage')
    about: Optional[Union[Thing, List[Thing]]] = Field(default=None, validation_alias=AliasChoices('about', 'https://schema.org/about'), serialization_alias='https://schema.org/about')
    recipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], ContactPoint, List[ContactPoint], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('recipient', 'https://schema.org/recipient'), serialization_alias='https://schema.org/recipient')
    language: Optional[Union[Language, List[Language]]] = Field(default=None, validation_alias=AliasChoices('language', 'https://schema.org/language'), serialization_alias='https://schema.org/language')
