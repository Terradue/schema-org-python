from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class CarUsageType(Enumeration):
    """
A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi.
    """
    type_: Literal['https://schema.org/CarUsageType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CarUsageType'),serialization_alias='class') # type: ignore
