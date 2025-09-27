from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MeasurementMethodEnum(Enumeration):
    """
Enumeration(s) for use with [[measurementMethod]].
    """
    class_: Literal['https://schema.org/MeasurementMethodEnum'] = Field('class', alias='class', serialization_alias='class') # type: ignore
