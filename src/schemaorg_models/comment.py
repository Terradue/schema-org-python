from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.creative_work import CreativeWork

class Comment(CreativeWork):
    """
A comment on an item - for example, a comment on a blog post. The comment's content is expressed via the [[text]] property, and its topic via [[about]], properties shared with all CreativeWorks.
    """
    type_: Literal['https://schema.org/Comment'] = Field(default='https://schema.org/Comment', alias='@type', serialization_alias='@type') # type: ignore
    parentItem: Optional[Union[CreativeWork, List[CreativeWork], "Comment", List["Comment"]]] = Field(default=None, validation_alias=AliasChoices('parentItem', 'https://schema.org/parentItem'), serialization_alias='https://schema.org/parentItem')
    downvoteCount: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('downvoteCount', 'https://schema.org/downvoteCount'), serialization_alias='https://schema.org/downvoteCount')
    sharedContent: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None, validation_alias=AliasChoices('sharedContent', 'https://schema.org/sharedContent'), serialization_alias='https://schema.org/sharedContent')
    upvoteCount: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('upvoteCount', 'https://schema.org/upvoteCount'), serialization_alias='https://schema.org/upvoteCount')
