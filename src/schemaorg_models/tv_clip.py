from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.clip import Clip

from schemaorg_models.tv_series import TVSeries

class TVClip(Clip):
    """
A short TV program or a segment/part of a TV program.
    """
    type_: Literal['https://schema.org/TVClip'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TVClip'),serialization_alias='class') # type: ignore
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = Field(default=None,validation_alias=AliasChoices('partOfTVSeries', 'https://schema.org/partOfTVSeries'),serialization_alias='https://schema.org/partOfTVSeries')
