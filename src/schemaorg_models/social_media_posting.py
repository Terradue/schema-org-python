from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.article import Article

from schemaorg_models.creative_work import CreativeWork

class SocialMediaPosting(Article):
    """
A post to a social media platform, including blog posts, tweets, Facebook posts, etc.
    """
    class_: Literal['https://schema.org/SocialMediaPosting'] = Field(default='https://schema.org/SocialMediaPosting', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    sharedContent: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None, validation_alias=AliasChoices('sharedContent', 'https://schema.org/sharedContent'), serialization_alias='https://schema.org/sharedContent')
