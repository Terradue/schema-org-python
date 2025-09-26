from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.service import Service

from schemaorg_models.creative_work import CreativeWork

class WebAPI(Service):
    """
An application programming interface accessible over Web/Internet technologies.
    """
    documentation: Optional[Union[HttpUrl, List[HttpUrl], CreativeWork, List[CreativeWork]]] = Field(default=None,validation_alias=AliasChoices('documentation', 'https://schema.org/documentation'),serialization_alias='https://schema.org/documentation')
    @field_serializer('documentation')
    def documentation2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

