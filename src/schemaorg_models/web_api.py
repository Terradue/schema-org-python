from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.service import Service

from schemaorg_models.creative_work import CreativeWork

class WebAPI(Service):
    """
An application programming interface accessible over Web/Internet technologies.
    """
    class_: Literal['https://schema.org/WebAPI'] = Field(default='https://schema.org/WebAPI', alias='class', serialization_alias='class') # type: ignore
    documentation: Optional[Union[HttpUrl, List[HttpUrl], CreativeWork, List[CreativeWork]]] = Field(default=None, validation_alias=AliasChoices('documentation', 'https://schema.org/documentation'), serialization_alias='https://schema.org/documentation')
    @field_serializer('documentation')
    def documentation2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

