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

class Comment(CreativeWork):
    '''
    A comment on an item - for example, a comment on a blog post. The comment's content is expressed via the [[text]] property, and its topic via [[about]], properties shared with all CreativeWorks.

    Attributes:
        parentItem: The parent of a question, answer or item in general. Typically used for Q/A discussion threads e.g. a chain of comments with the first comment being an [[Article]] or other [[CreativeWork]]. See also [[comment]] which points from something to a comment about it.
        downvoteCount: The number of downvotes this question, answer or comment has received from the community.
        sharedContent: A CreativeWork such as an image, video, or audio clip shared as part of this posting.
        upvoteCount: The number of upvotes this question, answer or comment has received from the community.
    '''
    class_: Literal['https://schema.org/Comment'] = Field( # type: ignore
        default='https://schema.org/Comment',
        alias='@type',
        serialization_alias='@type'
    )
    parentItem: Optional[Union['CreativeWork', List['CreativeWork'], 'Comment', List['Comment']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'parentItem',
            'https://schema.org/parentItem'
        ),
        serialization_alias='https://schema.org/parentItem'
    )
    downvoteCount: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'downvoteCount',
            'https://schema.org/downvoteCount'
        ),
        serialization_alias='https://schema.org/downvoteCount'
    )
    sharedContent: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sharedContent',
            'https://schema.org/sharedContent'
        ),
        serialization_alias='https://schema.org/sharedContent'
    )
    upvoteCount: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'upvoteCount',
            'https://schema.org/upvoteCount'
        ),
        serialization_alias='https://schema.org/upvoteCount'
    )
