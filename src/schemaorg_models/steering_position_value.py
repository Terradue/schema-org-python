from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.qualitative_value import QualitativeValue


class SteeringPositionValue(QualitativeValue):
    """
A value indicating a steering position.
    """
    type_: Literal['https://schema.org/SteeringPositionValue'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SteeringPositionValue'),serialization_alias='class') # type: ignore
