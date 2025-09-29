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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .item_list import ItemList

class HowToSection(CreativeWork):
    '''
    A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for making a pie crust within a pie recipe).

    Attributes:
        steps: A single step item (as HowToStep, text, document, video, etc.) or a HowToSection (originally misnamed 'steps'; 'step' is preferred).
    '''
    class_: Literal['https://schema.org/HowToSection'] = Field( # type: ignore
        default='https://schema.org/HowToSection',
        alias='@type',
        serialization_alias='@type'
    )
    steps: Optional[Union[str, List[str], 'CreativeWork', List['CreativeWork'], 'ItemList', List['ItemList']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
