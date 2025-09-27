from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.organization import Organization
from schemaorg_models.person import Person
from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.event import Event

class MusicComposition(CreativeWork):
    """
A musical composition.
    """
    class_: Literal['https://schema.org/MusicComposition'] = Field(default='https://schema.org/MusicComposition', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    recordedAs: Optional[Union["MusicRecording", List["MusicRecording"]]] = Field(default=None, validation_alias=AliasChoices('recordedAs', 'https://schema.org/recordedAs'), serialization_alias='https://schema.org/recordedAs')
    composer: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('composer', 'https://schema.org/composer'), serialization_alias='https://schema.org/composer')
    musicArrangement: Optional[Union["MusicComposition", List["MusicComposition"]]] = Field(default=None, validation_alias=AliasChoices('musicArrangement', 'https://schema.org/musicArrangement'), serialization_alias='https://schema.org/musicArrangement')
    lyrics: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None, validation_alias=AliasChoices('lyrics', 'https://schema.org/lyrics'), serialization_alias='https://schema.org/lyrics')
    includedComposition: Optional[Union["MusicComposition", List["MusicComposition"]]] = Field(default=None, validation_alias=AliasChoices('includedComposition', 'https://schema.org/includedComposition'), serialization_alias='https://schema.org/includedComposition')
    musicalKey: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('musicalKey', 'https://schema.org/musicalKey'), serialization_alias='https://schema.org/musicalKey')
    iswcCode: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('iswcCode', 'https://schema.org/iswcCode'), serialization_alias='https://schema.org/iswcCode')
    lyricist: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('lyricist', 'https://schema.org/lyricist'), serialization_alias='https://schema.org/lyricist')
    musicCompositionForm: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('musicCompositionForm', 'https://schema.org/musicCompositionForm'), serialization_alias='https://schema.org/musicCompositionForm')
    firstPerformance: Optional[Union[Event, List[Event]]] = Field(default=None, validation_alias=AliasChoices('firstPerformance', 'https://schema.org/firstPerformance'), serialization_alias='https://schema.org/firstPerformance')
