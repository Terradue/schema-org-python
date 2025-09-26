from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class WebSite(CreativeWork):
    """
A WebSite is a set of related web pages and other items typically served from a single web domain and accessible via URLs.
    """
    issn: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('issn', 'https://schema.org/issn'),serialization_alias='https://schema.org/issn')
