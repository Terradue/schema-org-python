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
    from .monetary_amount import MonetaryAmount
    from .duration import Duration
    from .item_list import ItemList
    from .how_to_tool import HowToTool
    from .how_to_step import HowToStep
    from .how_to_supply import HowToSupply
    from .quantitative_value import QuantitativeValue
    from .how_to_section import HowToSection

class HowTo(CreativeWork):
    '''
    Instructions that explain how to achieve a result by performing a sequence of steps.

    Attributes:
        prepTime: The length of time it takes to prepare the items to be used in instructions or a direction, in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        performTime: The length of time it takes to perform instructions or a direction (not including time to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        supply: A sub-property of instrument. A supply consumed when performing instructions or a direction.
        totalTime: The total time required to perform instructions or a direction (including time to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        step: A single step item (as HowToStep, text, document, video, etc.) or a HowToSection.
        estimatedCost: The estimated cost of the supply or supplies consumed when performing instructions.
        steps: A single step item (as HowToStep, text, document, video, etc.) or a HowToSection (originally misnamed 'steps'; 'step' is preferred).
        tool: A sub property of instrument. An object used (but not consumed) when performing instructions or a direction.
        yield_: The quantity that results by performing instructions. For example, a paper airplane, 10 personalized candles.
    '''
    class_: Literal['https://schema.org/HowTo'] = Field( # type: ignore
        default='https://schema.org/HowTo',
        alias='@type',
        serialization_alias='@type'
    )
    prepTime: Optional[Union['Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'prepTime',
            'https://schema.org/prepTime'
        ),
        serialization_alias='https://schema.org/prepTime'
    )
    performTime: Optional[Union['Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'performTime',
            'https://schema.org/performTime'
        ),
        serialization_alias='https://schema.org/performTime'
    )
    supply: Optional[Union['HowToSupply', List['HowToSupply'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'supply',
            'https://schema.org/supply'
        ),
        serialization_alias='https://schema.org/supply'
    )
    totalTime: Optional[Union['Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'totalTime',
            'https://schema.org/totalTime'
        ),
        serialization_alias='https://schema.org/totalTime'
    )
    step: Optional[Union[str, List[str], 'HowToStep', List['HowToStep'], 'CreativeWork', List['CreativeWork'], 'HowToSection', List['HowToSection']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'step',
            'https://schema.org/step'
        ),
        serialization_alias='https://schema.org/step'
    )
    estimatedCost: Optional[Union[str, List[str], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'estimatedCost',
            'https://schema.org/estimatedCost'
        ),
        serialization_alias='https://schema.org/estimatedCost'
    )
    steps: Optional[Union[str, List[str], 'CreativeWork', List['CreativeWork'], 'ItemList', List['ItemList']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'steps',
            'https://schema.org/steps'
        ),
        serialization_alias='https://schema.org/steps'
    )
    tool: Optional[Union[str, List[str], 'HowToTool', List['HowToTool']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tool',
            'https://schema.org/tool'
        ),
        serialization_alias='https://schema.org/tool'
    )
    yield_: Optional[Union[str, List[str], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'yield_',
            'https://schema.org/yield_'
        ),
        serialization_alias='https://schema.org/yield_'
    )
