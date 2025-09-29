from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .defined_term_set import DefinedTermSet

class DefinedTerm(Intangible):
    '''
    A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term.

    Attributes:
        termCode: A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]].
        inDefinedTermSet: A [[DefinedTermSet]] that contains this term.
    '''
    class_: Literal['https://schema.org/DefinedTerm'] = Field( # type: ignore
        default='https://schema.org/DefinedTerm',
        alias='@type',
        serialization_alias='@type'
    )
    termCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    inDefinedTermSet: Optional[Union[HttpUrl, List[HttpUrl], 'DefinedTermSet', List['DefinedTermSet']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
