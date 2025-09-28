from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
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
    from .how_to_supply import HowToSupply
    from .quantitative_value import QuantitativeValue
    from .how_to_tool import HowToTool
    from .how_to_step import HowToStep
    from .duration import Duration
    from .how_to_section import HowToSection
    from .item_list import ItemList
    from .monetary_amount import MonetaryAmount

class HowTo(CreativeWork):
    """
Instructions that explain how to achieve a result by performing a sequence of steps.
    """
    class_: Literal['https://schema.org/HowTo'] = Field( # type: ignore
        default='https://schema.org/HowTo',
        alias='@type',
        serialization_alias='@type'
    )
    prepTime: Optional[Union[Duration, List[Duration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'prepTime',
            'https://schema.org/prepTime'
        ),
        serialization_alias='https://schema.org/prepTime'
    )
    performTime: Optional[Union[Duration, List[Duration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'performTime',
            'https://schema.org/performTime'
        ),
        serialization_alias='https://schema.org/performTime'
    )
    supply: Optional[Union[HowToSupply, List[HowToSupply], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'supply',
            'https://schema.org/supply'
        ),
        serialization_alias='https://schema.org/supply'
    )
    totalTime: Optional[Union[Duration, List[Duration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'totalTime',
            'https://schema.org/totalTime'
        ),
        serialization_alias='https://schema.org/totalTime'
    )
    step: Optional[Union[str, List[str], HowToStep, List[HowToStep], CreativeWork, List[CreativeWork], HowToSection, List[HowToSection]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'step',
            'https://schema.org/step'
        ),
        serialization_alias='https://schema.org/step'
    )
    estimatedCost: Optional[Union[str, List[str], MonetaryAmount, List[MonetaryAmount]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'estimatedCost',
            'https://schema.org/estimatedCost'
        ),
        serialization_alias='https://schema.org/estimatedCost'
    )
    steps: Optional[Union[str, List[str], CreativeWork, List[CreativeWork], ItemList, List[ItemList]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'steps',
            'https://schema.org/steps'
        ),
        serialization_alias='https://schema.org/steps'
    )
    tool: Optional[Union[str, List[str], HowToTool, List[HowToTool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tool',
            'https://schema.org/tool'
        ),
        serialization_alias='https://schema.org/tool'
    )
    yield_: Optional[Union[str, List[str], QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'yield',
            'https://schema.org/yield'
        ),
        serialization_alias='https://schema.org/yield'
    )
