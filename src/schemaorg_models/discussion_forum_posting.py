from typing import Literal
from pydantic import Field
from schemaorg_models.social_media_posting import SocialMediaPosting


class DiscussionForumPosting(SocialMediaPosting):
    """
A posting to a discussion forum.
    """
    type_: Literal['https://schema.org/DiscussionForumPosting'] = Field(default='https://schema.org/DiscussionForumPosting', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
