from __future__ import annotations

from .service import Service    

from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.creative_work import CreativeWork

class WebAPI(Service):
    """
An application programming interface accessible over Web/Internet technologies.
    """
    class_: Literal['https://schema.org/WebAPI'] = Field( # type: ignore
        default='https://schema.org/WebAPI',
        alias='@type',
        serialization_alias='@type'
    )
    documentation: Optional[Union[HttpUrl, List[HttpUrl], CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'documentation',
            'https://schema.org/documentation'
        ),
        serialization_alias='https://schema.org/documentation'
    )
