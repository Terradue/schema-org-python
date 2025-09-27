from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Guide(CreativeWork):
    """
[[Guide]] is a page or article that recommends specific products or services, or aspects of a thing for a user to consider. A [[Guide]] may represent a Buying Guide and detail aspects of products or services for a user to consider. A [[Guide]] may represent a Product Guide and recommend specific products or services. A [[Guide]] may represent a Ranked List and recommend specific products or services with ranking.
    """
    class_: Literal['https://schema.org/Guide'] = Field(default='https://schema.org/Guide', alias='@type', serialization_alias='@type') # type: ignore
    reviewAspect: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('reviewAspect', 'https://schema.org/reviewAspect'), serialization_alias='https://schema.org/reviewAspect')
