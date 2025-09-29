from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .service import Service
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .creative_work import CreativeWork

class WebAPI(Service):
    '''
    An application programming interface accessible over Web/Internet technologies.

    Attributes:
        documentation: Further documentation describing the Web API in more detail.
    '''
    class_: Literal['https://schema.org/WebAPI'] = Field( # type: ignore
        default='https://schema.org/WebAPI',
        alias='@type',
        serialization_alias='@type'
    )
    documentation: Optional[Union[HttpUrl, List[HttpUrl], 'CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'documentation',
            'https://schema.org/documentation'
        ),
        serialization_alias='https://schema.org/documentation'
    )
