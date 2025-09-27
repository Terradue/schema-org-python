from typing import Literal
from pydantic import Field
from schemaorg_models.social_media_posting import SocialMediaPosting


class DiscussionForumPosting(SocialMediaPosting):
    """
A posting to a discussion forum.
    """
    class_: Literal['https://schema.org/DiscussionForumPosting'] = Field(default='https://schema.org/DiscussionForumPosting', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
