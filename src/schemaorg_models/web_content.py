from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class WebContent(CreativeWork):
    """
WebContent is a type representing all [[WebPage]], [[WebSite]] and [[WebPageElement]] content. It is sometimes the case that detailed distinctions between Web pages, sites and their parts are not always important or obvious. The  [[WebContent]] type makes it easier to describe Web-addressable content without requiring such distinctions to always be stated. (The intent is that the existing types [[WebPage]], [[WebSite]] and [[WebPageElement]] will eventually be declared as subtypes of [[WebContent]].)
    """
    class_: Literal['https://schema.org/WebContent'] = Field(default='https://schema.org/WebContent', alias='class', serialization_alias='class') # type: ignore
