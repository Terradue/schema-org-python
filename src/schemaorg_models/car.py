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
from .vehicle import Vehicle
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

class Car(Vehicle):
    '''
    A car is a wheeled, self-powered motor vehicle used for transportation.

    Attributes:
        roofLoad: The permitted total weight of cargo and installations (e.g. a roof rack) on top of the vehicle.\
\
Typical unit code(s): KGM for kilogram, LBR for pound\
\
* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\
* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]]\
* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        acrissCode: The ACRISS Car Classification Code is a code used by many car rental companies, for classifying vehicles. ACRISS stands for Association of Car Rental Industry Systems and Standards.
    '''
    class_: Literal['https://schema.org/Car'] = Field( # type: ignore
        default='https://schema.org/Car',
        alias='@type',
        serialization_alias='@type'
    )
    roofLoad: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'roofLoad',
            'https://schema.org/roofLoad'
        ),
        serialization_alias='https://schema.org/roofLoad'
    )
    acrissCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acrissCode',
            'https://schema.org/acrissCode'
        ),
        serialization_alias='https://schema.org/acrissCode'
    )
