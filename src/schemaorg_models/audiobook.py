from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.audio_object import AudioObject

from schemaorg_models.duration import Duration
from schemaorg_models.quantitative_value import QuantitativeValue
from schemaorg_models.person import Person

class Audiobook(AudioObject):
    """
An audiobook.
    """
    class_: Literal['https://schema.org/Audiobook'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    duration: Optional[Union[Duration, List[Duration], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('duration', 'https://schema.org/duration'), serialization_alias='https://schema.org/duration')
    readBy: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('readBy', 'https://schema.org/readBy'), serialization_alias='https://schema.org/readBy')
