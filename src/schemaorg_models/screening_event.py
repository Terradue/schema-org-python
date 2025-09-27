from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class ScreeningEvent(Event):
    """
A screening of a movie or other video.
    """
    class_: Literal['https://schema.org/ScreeningEvent'] = Field(default='https://schema.org/ScreeningEvent', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    subtitleLanguage: Optional[Union["Language", List["Language"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('subtitleLanguage', 'https://schema.org/subtitleLanguage'), serialization_alias='https://schema.org/subtitleLanguage')
    videoFormat: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('videoFormat', 'https://schema.org/videoFormat'), serialization_alias='https://schema.org/videoFormat')
    workPresented: Optional[Union["Movie", List["Movie"]]] = Field(default=None, validation_alias=AliasChoices('workPresented', 'https://schema.org/workPresented'), serialization_alias='https://schema.org/workPresented')
