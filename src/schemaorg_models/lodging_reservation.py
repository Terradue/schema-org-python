from typing import List, Literal, Optional, Union
from datetime import datetime, time
from pydantic import AliasChoices, Field
from schemaorg_models.reservation import Reservation

from schemaorg_models.quantitative_value import QuantitativeValue
from schemaorg_models.qualitative_value import QualitativeValue

class LodgingReservation(Reservation):
    """
A reservation for lodging at a hotel, motel, inn, etc.\
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.
    """
    type_: Literal['https://schema.org/LodgingReservation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/LodgingReservation'),serialization_alias='class') # type: ignore
    checkoutTime: Optional[Union[datetime, List[datetime], time, List[time]]] = Field(default=None,validation_alias=AliasChoices('checkoutTime', 'https://schema.org/checkoutTime'),serialization_alias='https://schema.org/checkoutTime')
    numAdults: Optional[Union[QuantitativeValue, List[QuantitativeValue], int, List[int]]] = Field(default=None,validation_alias=AliasChoices('numAdults', 'https://schema.org/numAdults'),serialization_alias='https://schema.org/numAdults')
    checkinTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('checkinTime', 'https://schema.org/checkinTime'),serialization_alias='https://schema.org/checkinTime')
    lodgingUnitType: Optional[Union[str, List[str], QualitativeValue, List[QualitativeValue]]] = Field(default=None,validation_alias=AliasChoices('lodgingUnitType', 'https://schema.org/lodgingUnitType'),serialization_alias='https://schema.org/lodgingUnitType')
    lodgingUnitDescription: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('lodgingUnitDescription', 'https://schema.org/lodgingUnitDescription'),serialization_alias='https://schema.org/lodgingUnitDescription')
    numChildren: Optional[Union[QuantitativeValue, List[QuantitativeValue], int, List[int]]] = Field(default=None,validation_alias=AliasChoices('numChildren', 'https://schema.org/numChildren'),serialization_alias='https://schema.org/numChildren')
