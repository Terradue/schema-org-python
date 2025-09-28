from __future__ import annotations

from .intangible import Intangible    

from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class DefinedTerm(Intangible):
    """
A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term.
    """
    class_: Literal['https://schema.org/DefinedTerm'] = Field( # type: ignore
        default='https://schema.org/DefinedTerm',
        alias='@type',
        serialization_alias='@type'
    )
    termCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'termCode',
            'https://schema.org/termCode'
        ),
        serialization_alias='https://schema.org/termCode'
    )
    inDefinedTermSet: Optional[Union[HttpUrl, List[HttpUrl], "DefinedTermSet", List["DefinedTermSet"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inDefinedTermSet',
            'https://schema.org/inDefinedTermSet'
        ),
        serialization_alias='https://schema.org/inDefinedTermSet'
    )
