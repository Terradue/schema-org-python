from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action

from schemaorg_models.hyper_toc_entry import HyperTocEntry

class SeekToAction(Action):
    """
This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within a [[VideoObject]], typically represented with a URL template structure.
    """
    startOffset: Optional[Union[float, List[float], HyperTocEntry, List[HyperTocEntry]]] = Field(default=None,validation_alias=AliasChoices('startOffset', 'https://schema.org/startOffset'),serialization_alias='https://schema.org/startOffset')
