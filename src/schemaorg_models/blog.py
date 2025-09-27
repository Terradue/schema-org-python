from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Blog(CreativeWork):
    """
A [blog](https://en.wikipedia.org/wiki/Blog), sometimes known as a "weblog". Note that the individual posts ([[BlogPosting]]s) in a [[Blog]] are often colloquially referred to by the same term.
    """
    class_: Literal['https://schema.org/Blog'] = Field(default='https://schema.org/Blog', alias='@type', serialization_alias='@type') # type: ignore
    issn: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('issn', 'https://schema.org/issn'), serialization_alias='https://schema.org/issn')
    blogPost: Optional[Union["BlogPosting", List["BlogPosting"]]] = Field(default=None, validation_alias=AliasChoices('blogPost', 'https://schema.org/blogPost'), serialization_alias='https://schema.org/blogPost')
    blogPosts: Optional[Union["BlogPosting", List["BlogPosting"]]] = Field(default=None, validation_alias=AliasChoices('blogPosts', 'https://schema.org/blogPosts'), serialization_alias='https://schema.org/blogPosts')
