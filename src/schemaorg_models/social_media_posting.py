from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.article import Article

from schemaorg_models.creative_work import CreativeWork

class SocialMediaPosting(Article):
    """
A post to a social media platform, including blog posts, tweets, Facebook posts, etc.
    """
    sharedContent: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None,validation_alias=AliasChoices('sharedContent', 'https://schema.org/sharedContent'),serialization_alias='https://schema.org/sharedContent')
