from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.social_media_posting import SocialMediaPosting


class DiscussionForumPosting(SocialMediaPosting):
    """
A posting to a discussion forum.
    """
    type_: Literal['https://schema.org/DiscussionForumPosting'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DiscussionForumPosting'),serialization_alias='class') # type: ignore
