from typing import Literal
from pydantic import Field
from schemaorg_models.social_media_posting import SocialMediaPosting


class BlogPosting(SocialMediaPosting):
    """
A blog post.
    """
    type_: Literal['https://schema.org/BlogPosting'] = Field(default='https://schema.org/BlogPosting', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
