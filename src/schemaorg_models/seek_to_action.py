from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action

from schemaorg_models.hyper_toc_entry import HyperTocEntry

class SeekToAction(Action):
    """
This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within a [[VideoObject]], typically represented with a URL template structure.
    """
    type_: Literal['https://schema.org/SeekToAction'] = Field(default='https://schema.org/SeekToAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    startOffset: Optional[Union[float, List[float], HyperTocEntry, List[HyperTocEntry]]] = Field(default=None, validation_alias=AliasChoices('startOffset', 'https://schema.org/startOffset'), serialization_alias='https://schema.org/startOffset')
