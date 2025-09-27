from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.clip import Clip

from schemaorg_models.tv_series import TVSeries

class TVClip(Clip):
    """
A short TV program or a segment/part of a TV program.
    """
    type_: Literal['https://schema.org/TVClip'] = Field(default='https://schema.org/TVClip', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = Field(default=None, validation_alias=AliasChoices('partOfTVSeries', 'https://schema.org/partOfTVSeries'), serialization_alias='https://schema.org/partOfTVSeries')
