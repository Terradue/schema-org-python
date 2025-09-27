from typing import Literal
from pydantic import Field
from schemaorg_models.article import Article


class SatiricalArticle(Article):
    """
An [[Article]] whose content is primarily [[satirical]](https://en.wikipedia.org/wiki/Satire) in nature, i.e. unlikely to be literally true. A satirical article is sometimes but not necessarily also a [[NewsArticle]]. [[ScholarlyArticle]]s are also sometimes satirized.
    """
    type_: Literal['https://schema.org/SatiricalArticle'] = Field(default='https://schema.org/SatiricalArticle', alias='@type', serialization_alias='@type') # type: ignore
