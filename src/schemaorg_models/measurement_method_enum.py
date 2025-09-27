from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class MeasurementMethodEnum(Enumeration):
    """
Enumeration(s) for use with [[measurementMethod]].
    """
    type_: Literal['https://schema.org/MeasurementMethodEnum'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MeasurementMethodEnum'),serialization_alias='class') # type: ignore
