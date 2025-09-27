from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action

from schemaorg_models.hyper_toc_entry import HyperTocEntry

class SeekToAction(Action):
    """
This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within a [[VideoObject]], typically represented with a URL template structure.
    """
    class_: Literal['https://schema.org/SeekToAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    startOffset: Optional[Union[float, List[float], HyperTocEntry, List[HyperTocEntry]]] = Field(default=None,validation_alias=AliasChoices('startOffset', 'https://schema.org/startOffset'), serialization_alias='https://schema.org/startOffset')
