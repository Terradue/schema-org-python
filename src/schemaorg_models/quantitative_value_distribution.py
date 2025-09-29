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
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .duration import Duration
    from .quantitative_value import QuantitativeValue

class QuantitativeValueDistribution(StructuredValue):
    '''
    A statistical distribution of values.

    Attributes:
        median: The median value.
        percentile75: The 75th percentile value.
        percentile25: The 25th percentile value.
        percentile90: The 90th percentile value.
        percentile10: The 10th percentile value.
        duration: The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
    '''
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
    duration: Optional[Union['Duration', List['Duration'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duration',
            'https://schema.org/duration'
        ),
        serialization_alias='https://schema.org/duration'
    )
