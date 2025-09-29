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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .book_format_type import BookFormatType
    from .person import Person

class Book(CreativeWork):
    """
A book.
    """
    class_: Literal['https://schema.org/Book'] = Field( # type: ignore
        default='https://schema.org/Book',
        alias='@type',
        serialization_alias='@type'
    )
    abridged: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'abridged',
            'https://schema.org/abridged'
        ),
        serialization_alias='https://schema.org/abridged'
    )
    bookFormat: Optional[Union["BookFormatType", List["BookFormatType"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bookFormat',
            'https://schema.org/bookFormat'
        ),
        serialization_alias='https://schema.org/bookFormat'
    )
    isbn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isbn',
            'https://schema.org/isbn'
        ),
        serialization_alias='https://schema.org/isbn'
    )
    numberOfPages: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfPages',
            'https://schema.org/numberOfPages'
        ),
        serialization_alias='https://schema.org/numberOfPages'
    )
    illustrator: Optional[Union["Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'illustrator',
            'https://schema.org/illustrator'
        ),
        serialization_alias='https://schema.org/illustrator'
    )
    bookEdition: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bookEdition',
            'https://schema.org/bookEdition'
        ),
        serialization_alias='https://schema.org/bookEdition'
    )
