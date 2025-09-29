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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .blog_posting import BlogPosting

class Blog(CreativeWork):
    '''
    A [blog](https://en.wikipedia.org/wiki/Blog), sometimes known as a "weblog". Note that the individual posts ([[BlogPosting]]s) in a [[Blog]] are often colloquially referred to by the same term.

    Attributes:
        issn: The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication.
        blogPost: A posting that is part of this blog.
        blogPosts: Indicates a post that is part of a [[Blog]]. Note that historically, what we term a "Blog" was once known as a "weblog", and that what we term a "BlogPosting" is now often colloquially referred to as a "blog".
    '''
    class_: Literal['https://schema.org/Blog'] = Field( # type: ignore
        default='https://schema.org/Blog',
        alias='@type',
        serialization_alias='@type'
    )
    issn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    blogPost: Optional[Union['BlogPosting', List['BlogPosting']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    blogPosts: Optional[Union['BlogPosting', List['BlogPosting']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
