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
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .duration import Duration

class QuantitativeValueDistribution(StructuredValue):
    """
A statistical distribution of values.
    """
    class_: Literal['https://schema.org/QuantitativeValueDistribution'] = Field( # type: ignore
        default='https://schema.org/QuantitativeValueDistribution',
        alias='@type',
        serialization_alias='@type'
    )
    median: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'median',
            'https://schema.org/median'
        ),
        serialization_alias='https://schema.org/median'
    )
    percentile75: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'percentile75',
            'https://schema.org/percentile75'
        ),
        serialization_alias='https://schema.org/percentile75'
    )
    percentile25: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'percentile25',
            'https://schema.org/percentile25'
        ),
        serialization_alias='https://schema.org/percentile25'
    )
    percentile90: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'percentile90',
            'https://schema.org/percentile90'
        ),
        serialization_alias='https://schema.org/percentile90'
    )
    percentile10: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'percentile10',
            'https://schema.org/percentile10'
        ),
        serialization_alias='https://schema.org/percentile10'
    )
    duration: Optional[Union[Duration, List[Duration], QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duration',
            'https://schema.org/duration'
        ),
        serialization_alias='https://schema.org/duration'
    )
