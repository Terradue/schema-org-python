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
from .defined_term import DefinedTerm
from .creative_work import CreativeWork

class DefinedTermSet(CreativeWork):
    """
A set of defined terms, for example a set of categories or a classification scheme, a glossary, dictionary or enumeration.
    """
    class_: Literal['https://schema.org/DefinedTermSet'] = Field( # type: ignore
        default='https://schema.org/DefinedTermSet',
        alias='@type',
        serialization_alias='@type'
    )
    hasDefinedTerm: Optional[Union[DefinedTerm, List[DefinedTerm]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasDefinedTerm',
            'https://schema.org/hasDefinedTerm'
        ),
        serialization_alias='https://schema.org/hasDefinedTerm'
    )
