from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.person import Person

class ComicStory(CreativeWork):
    """
The term "story" is any indivisible, re-printable
    	unit of a comic, including the interior stories, covers, and backmatter. Most
    	comics have at least two stories: a cover (ComicCoverArt) and an interior story.
    """
    class_: Literal['https://schema.org/ComicStory'] = Field(default='https://schema.org/ComicStory', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    penciler: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('penciler', 'https://schema.org/penciler'), serialization_alias='https://schema.org/penciler')
    inker: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('inker', 'https://schema.org/inker'), serialization_alias='https://schema.org/inker')
    letterer: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('letterer', 'https://schema.org/letterer'), serialization_alias='https://schema.org/letterer')
    colorist: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('colorist', 'https://schema.org/colorist'), serialization_alias='https://schema.org/colorist')
    artist: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('artist', 'https://schema.org/artist'), serialization_alias='https://schema.org/artist')
