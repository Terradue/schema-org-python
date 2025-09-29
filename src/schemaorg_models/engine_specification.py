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
    from .qualitative_value import QualitativeValue
    from .quantitative_value import QuantitativeValue

class EngineSpecification(StructuredValue):
    '''
    Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities.

    Attributes:
        fuelType: The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.
        engineType: The type of engine or engines powering the vehicle.
        engineDisplacement: The volume swept by all of the pistons inside the cylinders of an internal combustion engine in a single movement. \
\
Typical unit code(s): CMQ for cubic centimeter, LTR for liters, INQ for cubic inches\
* Note 1: You can link to information about how the given value has been determined using the [[valueReference]] property.\
* Note 2: You can use [[minValue]] and [[maxValue]] to indicate ranges.
        enginePower: The power of the vehicle's engine.
    Typical unit code(s): KWT for kilowatt, BHP for brake horsepower, N12 for metric horsepower (PS, with 1 PS = 735,49875 W)\
\
* Note 1: There are many different ways of measuring an engine's power. For an overview, see  [http://en.wikipedia.org/wiki/Horsepower#Engine\\_power\\_test\\_codes](http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes).\
* Note 2: You can link to information about how the given value has been determined using the [[valueReference]] property.\
* Note 3: You can use [[minValue]] and [[maxValue]] to indicate ranges.
        torque: The torque (turning force) of the vehicle's engine.\
\
Typical unit code(s): NU for newton metre (N m), F17 for pound-force per foot, or F48 for pound-force per inch\
\
* Note 1: You can link to information about how the given value has been determined (e.g. reference RPM) using the [[valueReference]] property.\
* Note 2: You can use [[minValue]] and [[maxValue]] to indicate ranges.
    '''
    class_: Literal['https://schema.org/EngineSpecification'] = Field( # type: ignore
        default='https://schema.org/EngineSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    fuelType: Optional[Union[str, List[str], 'QualitativeValue', List['QualitativeValue'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fuelType',
            'https://schema.org/fuelType'
        ),
        serialization_alias='https://schema.org/fuelType'
    )
    engineType: Optional[Union[HttpUrl, List[HttpUrl], str, List[str], 'QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'engineType',
            'https://schema.org/engineType'
        ),
        serialization_alias='https://schema.org/engineType'
    )
    engineDisplacement: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'engineDisplacement',
            'https://schema.org/engineDisplacement'
        ),
        serialization_alias='https://schema.org/engineDisplacement'
    )
    enginePower: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'enginePower',
            'https://schema.org/enginePower'
        ),
        serialization_alias='https://schema.org/enginePower'
    )
    torque: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'torque',
            'https://schema.org/torque'
        ),
        serialization_alias='https://schema.org/torque'
    )
