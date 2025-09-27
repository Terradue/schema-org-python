from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class CarUsageType(Enumeration):
    """
A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi.
    """
    class_: Literal['https://schema.org/CarUsageType'] = Field('class', alias='class', serialization_alias='class') # type: ignore
