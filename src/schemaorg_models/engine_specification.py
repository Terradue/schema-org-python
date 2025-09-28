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
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .qualitative_value import QualitativeValue

class EngineSpecification(StructuredValue):
    """
Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities.
    """
    class_: Literal['https://schema.org/EngineSpecification'] = Field( # type: ignore
        default='https://schema.org/EngineSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    fuelType: Optional[Union[str, List[str], QualitativeValue, List[QualitativeValue], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fuelType',
            'https://schema.org/fuelType'
        ),
        serialization_alias='https://schema.org/fuelType'
    )
    engineType: Optional[Union[HttpUrl, List[HttpUrl], str, List[str], QualitativeValue, List[QualitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'engineType',
            'https://schema.org/engineType'
        ),
        serialization_alias='https://schema.org/engineType'
    )
    engineDisplacement: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'engineDisplacement',
            'https://schema.org/engineDisplacement'
        ),
        serialization_alias='https://schema.org/engineDisplacement'
    )
    enginePower: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'enginePower',
            'https://schema.org/enginePower'
        ),
        serialization_alias='https://schema.org/enginePower'
    )
    torque: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'torque',
            'https://schema.org/torque'
        ),
        serialization_alias='https://schema.org/torque'
    )
