from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import AliasChoices, Field
from schemaorg_models.property_value import PropertyValue

from schemaorg_models.opening_hours_specification import OpeningHoursSpecification

class LocationFeatureSpecification(PropertyValue):
    """
Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality.
    """
    class_: Literal['https://schema.org/LocationFeatureSpecification'] = Field(default='https://schema.org/LocationFeatureSpecification', alias='class', serialization_alias='class') # type: ignore
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'), serialization_alias='https://schema.org/validFrom')
    hoursAvailable: Optional[Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]] = Field(default=None, validation_alias=AliasChoices('hoursAvailable', 'https://schema.org/hoursAvailable'), serialization_alias='https://schema.org/hoursAvailable')
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None, validation_alias=AliasChoices('validThrough', 'https://schema.org/validThrough'), serialization_alias='https://schema.org/validThrough')
