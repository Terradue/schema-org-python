from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .action import Action
from .hyper_toc_entry import HyperTocEntry

class SeekToAction(Action):
    """
This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within a [[VideoObject]], typically represented with a URL template structure.
    """
    class_: Literal['https://schema.org/SeekToAction'] = Field( # type: ignore
        default='https://schema.org/SeekToAction',
        alias='@type',
        serialization_alias='@type'
    )
    startOffset: Optional[Union[float, List[float], HyperTocEntry, List[HyperTocEntry]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startOffset',
            'https://schema.org/startOffset'
        ),
        serialization_alias='https://schema.org/startOffset'
    )
