from __future__ import annotations

from .creative_work import CreativeWork    

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
from schemaorg_models.defined_term import DefinedTerm

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
