from __future__ import annotations
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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .media_object import MediaObject
    from .duration import Duration
    from .how_to_tool import HowToTool
    from .how_to_supply import HowToSupply

class HowToDirection(CreativeWork):
    """
A direction indicating a single action to do in the instructions for how to achieve a result.
    """
    class_: Literal['https://schema.org/HowToDirection'] = Field( # type: ignore
        default='https://schema.org/HowToDirection',
        alias='@type',
        serialization_alias='@type'
    )
    beforeMedia: Optional[Union["MediaObject", List["MediaObject"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'beforeMedia',
            'https://schema.org/beforeMedia'
        ),
        serialization_alias='https://schema.org/beforeMedia'
    )
    prepTime: Optional[Union["Duration", List["Duration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'prepTime',
            'https://schema.org/prepTime'
        ),
        serialization_alias='https://schema.org/prepTime'
    )
    supply: Optional[Union["HowToSupply", List["HowToSupply"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'supply',
            'https://schema.org/supply'
        ),
        serialization_alias='https://schema.org/supply'
    )
    performTime: Optional[Union["Duration", List["Duration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'performTime',
            'https://schema.org/performTime'
        ),
        serialization_alias='https://schema.org/performTime'
    )
    totalTime: Optional[Union["Duration", List["Duration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'totalTime',
            'https://schema.org/totalTime'
        ),
        serialization_alias='https://schema.org/totalTime'
    )
    duringMedia: Optional[Union[HttpUrl, List[HttpUrl], "MediaObject", List["MediaObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duringMedia',
            'https://schema.org/duringMedia'
        ),
        serialization_alias='https://schema.org/duringMedia'
    )
    tool: Optional[Union[str, List[str], "HowToTool", List["HowToTool"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tool',
            'https://schema.org/tool'
        ),
        serialization_alias='https://schema.org/tool'
    )
    afterMedia: Optional[Union[HttpUrl, List[HttpUrl], "MediaObject", List["MediaObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'afterMedia',
            'https://schema.org/afterMedia'
        ),
        serialization_alias='https://schema.org/afterMedia'
    )
