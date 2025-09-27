from typing import Literal
from pydantic import Field
from schemaorg_models.social_media_posting import SocialMediaPosting


class DiscussionForumPosting(SocialMediaPosting):
    """
A posting to a discussion forum.
    """
    class_: Literal['https://schema.org/DiscussionForumPosting'] = Field(default='https://schema.org/DiscussionForumPosting', alias='class', serialization_alias='class') # type: ignore
